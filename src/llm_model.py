import os
import json
import google.generativeai as palm_genai


class LLM_Model:
    """
    A class that utilizes an LLM (Large Language Model) to track dialog state.
    """

    def __init__(self, api_key:str=None):
        if api_key is None:
            with open(".env", "r") as f:
                self.api_key = f.read().strip()
        else:
            self.api_key = api_key
        self.palm = palm_genai
        self.palm.configure(api_key=self.api_key)
        self.model = self.palm.GenerativeModel() #model="gemini-flash") #or "gemini-pro" if you have access
            
        self.dialog_history = ""
        self.act_type_list = [
            "Attraction-Inform",
            "Attraction-NoOffer",
            "Attraction-Recommend",
            "Attraction-Select",
            "Booking-Book",
            "Booking-Inform",
            "Booking-NoBook",
            "Hospital-Inform",
            "Hotel-Inform",
            "Hotel-NoOffer",
            "Hotel-Recommend",
            "Hotel-Select",
            "Police-Inform",
            "Restaurant-Inform",
            "Restaurant-NoOffer",
            "Restaurant-Recommend",
            "Restaurant-Select",
            "Taxi-Inform",
            "Train-Inform",
            "Train-NoOffer",
            "Train-OfferBook",
            "Train-OfferBooked",
            "Train-Select",
        ]
        self.slot_type_list = [
            "address",
            "area",
            "arriveby",
            "bookday",
            "bookpeople",
            "bookstay",
            "booktime",
            "choice",
            "day",
            "department",
            "departure",
            "destination",
            "duration",
            "entrancefee",
            "food",
            "leaveat",
            "name",
            "openhours",
            "phone",
            "postcode",
            "price",
            "pricerange",
            "ref",
            "stars",
            "trainid",
            "type",
        ]

    def _build_prompt(self, current_turn):
        """
        Constructs the prompt for the LLM based on dialog history and current turn.
        """
        prompt = f"""
        You are a system that tracks conversation states. Given the following conversation history and current turn, extract the current conversation state as a JSON dictionary:

        Act Type List:
        {self.act_type_list}

        Slot Type List:
        {self.slot_type_list}

        Conversation History:
        {self.dialog_history}

        Current Turn:
        {current_turn}

        Return Conversation state (JSON) for current turn:
        {{act_type: [act_value, ...], slot_type: {{slot_1: slot_value_1, slot_2: slot_value_2, ...}}}}
        """

        return prompt

    def track_dialog_state(self, current_turn):
        """
        Tracks dialog state by calling the LLM with a constructed prompt.
        """

        prompt = self._build_prompt(current_turn)
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        defaults = {
            "model": "gemini-1.5-flash",  # Replace with actual model endpoint when available
            "prompt": prompt,
            "temperature": 0.0,
            "max_output_tokens": 256,
        }

        response = self.model.generate_content(prompt)

        if response.prompt_feedback and response.prompt_feedback.block_reason:
            print(f"Prompt was blocked: {response.prompt_feedback.block_reason}")
            return None
        if response.text is None:
            print("No text generated in response.")
            return None

        # try:
        #     dialog_state = json.loads(response.text)
        #     return dialog_state
        # except json.JSONDecodeError:
        #     print(f"Invalid JSON response: {response.text}") #print the invalid json for debug
        #     return response.text
        
        return response.text

    def main(self):
        """
        Main loop for user interaction and dialog state tracking.
        """

        while True:
            current_turn = input("Input current turn (or type 'q' to quit): ")
            if current_turn.lower() == "q":
                break
            dialog_state = self.track_dialog_state(current_turn)
            if dialog_state:
                print("Extracted dialog state for current turn:")
                print(dialog_state)
            else:
                print("Could not extract dialog state.")
            self.dialog_history += f"User: {current_turn}\n"


if __name__ == "__main__":
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Please set your GEMINI_API_KEY environment variable.")

    model = LLM_Model(api_key)
    model.main()
