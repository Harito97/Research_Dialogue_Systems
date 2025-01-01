**Dialogue Systems**

Dialogue systems (also known as dialogue agents or chatbots) are a crucial area of natural language processing (NLP) and human-computer interaction (HCI). This report details the issues, problems, and general methods related to dialogue systems, based on two documents: [Book_ Chapter_15](../../references/Book_%20Chapter_15.pdf) & [Slides_ 24_Dialogue_May_6_2021](../../references/Slides_%2024_Dialogue_May_6_2021.pdf).

# Problems

## Introduction

Dialogue systems are systems capable of engaging in conversations with users, simulating natural human-to-human interaction. They have numerous real-world applications, including:

*   **Personal virtual assistants:** Siri, Alexa, Cortana, Google Assistant
*   **Entertainment:** Chatbots can converse, tell jokes, and provide information.
*   **Task support:** Scheduling appointments, booking flights, making restaurant reservations
*   **Healthcare:** Providing psychological support

## Classification

There are two main types of dialogue systems:

1.  **Chatbots:** Their goal is to simulate natural conversation, often for entertainment or psychological support.
2.  **Task-oriented dialogue agents:** Their goal is to help users complete a specific task, such as booking a flight or making a restaurant reservation.

## Characteristics of Natural Dialogue

To build effective dialogue systems, it is essential to understand the characteristics of natural human-to-human conversation. Some important features include:

*   **Turns:** Each turn is a contribution by one speaker in the conversation.
*   **Turn-taking issues:** Determining when a turn begins and ends. Interruptions are also a consideration.
*   **Language as an action:** Each turn is a speech act performed by the speaker, such as asserting, requesting, promising, or thanking.
*   **Implicit understanding:** Speakers and listeners need to establish common ground, using cues to ensure mutual understanding (grounding).
*   **Dialogue structure:** Dialogue has a structure, such as question-answer pairs and proposal-acceptance/rejection. There are also subdialogues, such as error correction and clarification.
*   **Dialogue initiative:** Dialogue can be initiated by one person (e.g., an interview) or by both parties (mixed initiative).
*   **Inference:** Listeners often must infer from the information provided to fully understand the speaker's meaning.

# Methods

## Rule-based Chatbots

*   ELIZA (1966) and PARRY (1971) are two classic examples of rule-based chatbots.
*   ELIZA simulated a Rogerian psychotherapist, reflecting the user's statements to create a sense of conversation.
*   PARRY simulated a person with paranoid schizophrenia, using a more complex rule system to generate responses.
*   Both ELIZA and PARRY used patterns and transformation rules to generate responses.
*   **Limitations:** Expensive, prone to errors, and difficult to scale.

## Corpus-based Chatbots

*   Use large dialogue datasets to train models.
*   Two main architectures:
    *   **Retrieval-based:** Find the most suitable answer from the database based on similarity.
    *   **Generation-based:** Use language models or encoder-decoder models to generate new responses.
*   **Datasets:**
    *   Recordings of phone calls and movie dialogues
    *   Data from social media platforms such as Twitter, Reddit, and Weibo.
    *   Human-created data, such as Topical-Chat and EMPATHETICDIALOGUES.
*   **Advantages:** More flexible than rule-based chatbots.
*   **Limitations:**
    *   **Prone to repetition and becoming boring.**
    *   **Susceptible to bias in the training data, potentially generating inappropriate responses.**

## Frame-based Architecture (GUS)

*   **Goal:** Help users complete specific tasks.
*   **Architecture:** Uses frames with slots and values to represent the user's intent.
*   **Example:** A flight booking frame has slots such as ORIGIN, DESTINATION, DEPARTURE DATE, and DEPARTURE TIME.
*   **Operation:** The system asks the user questions to fill the slots in the frame.

## Dialogue-State Architecture

*   **Extends frame-based architecture:**
    *   Uses dialogue acts.
    *   Uses machine learning for natural language processing.
    *   Generates more natural responses.
*   **Components:**
    *   NLU (Natural Language Understanding): Extracts information from the user's speech.
    *   Dialogue state tracker: Tracks the current state of the dialogue.
    *   Dialogue policy: Determines the system's next action.
    *   NLG (Natural Language Generation): Generates responses in natural language.
*   **Dialogue acts:** Represent dialogue actions and grounding. Examples: INFORM, REQUEST, CONFIRM.
*   **Dialogue state tracking:** Determines the dialogue act and updates the frame based on user input.
*   **Error correction detection:** Identifies when the user corrects the system, using lexical, semantic, and phonetic features.
*   **Dialogue policy:**
    *   Determines the next action based on the dialogue state.
    *   **Confirmation:** Ensures the system understands the user.
        *   **Explicit:** Directly asking the user.
        *   **Implicit:** Repeating the understood information.
    *   **Rejection:** When the system does not understand the user's input.
*   **Natural language generation:**
    *   **Content planning:** Determines the content to be conveyed.
    *   **Sentence realization:** Creates sentences based on the content.
    *   **Delexicalization:** Replaces specific values with generic tags to increase generalization.
    *   **Generating clarification questions:** When the system needs more information.

# Dialogue System Evaluation

*   **Chatbots:** Primarily evaluated by humans, through evaluations by participants or observers.
*   **Task-oriented dialogue systems:**
    *   **End-to-end evaluation:** Evaluates the ability to complete tasks.
    *   **Slot Error Rate:** Evaluates the accuracy of information extraction.
*   Other evaluation criteria:
    *   Efficiency: Dialogue time, number of turns, number of queries.
    *   Quality: Number of rejections, number of times the user has to interrupt.

# Design and Ethical Considerations

*   **User-centered design:**
    *   Research users and tasks.
    *   Build simulations and prototypes (e.g., Wizard of Oz study).
    *   Iteratively test the design with users.
*   **Ethical considerations:**
    *   **User safety:** The system should provide accurate information and avoid causing harm.
    *   **Abusive and discriminatory language:** The system should avoid generating offensive or discriminatory responses.
    *   **Information leakage:** Protecting users' personal information.

# Conclusion

Dialogue systems are a fascinating and challenging research area. Understanding the issues, problems, and general methods related to dialogue systems is crucial for building effective, safe, and beneficial systems for users.