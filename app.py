import streamlit as st

# Define questions for each section
transformational_questions = [
    "My leader acts in ways that build my respect.",
    "My leader shows a strong sense of purpose in their actions.",
    "My leader is reliable and instills trust.",
    "My leader demonstrates values that align with our team’s mission.",
    "My leader is seen as a role model in our team.",
    "My leader consistently behaves with integrity.",
    "My leader inspires me to achieve my goals.",
    "My leader communicates a vision that is motivating.",
    "My leader helps me find meaning in my work.",
    "My leader encourages me to approach tasks from different perspectives.",
    "My leader helps me learn from mistakes without judgment.",
    "My leader promotes creativity within the team.",
    "My leader provides personal coaching to support my development.",
    "My leader considers my personal needs when assigning tasks.",
    "My leader recognizes my unique strengths and encourages me to use them."
]


transactional_questions = [
    "My leader makes clear the rewards I can expect for good performance.",
    "My leader recognizes when I meet or exceed expectations.",
    "My leader communicates rewards in a way that motivates me.",
    "My leader addresses issues quickly when they arise.",
    "My leader is proactive about monitoring work quality.",
    "My leader checks in regularly to ensure we are meeting standards.",
    "My leader addresses issues only when they are critical.",
    "My leader takes action after problems have already escalated.",
    "My leader provides feedback only when absolutely necessary."
]

laissez_faire_questions = [
    "My leader is often unavailable when I need help.",
    "My leader avoids making important decisions.",
    "My leader takes a hands-off approach and rarely intervenes."
]

team_effectiveness_questions = [
    "My leader creates a positive team culture that motivates me.",
    "My leader effectively aligns our team with the organization’s goals.",
    "My leader fosters a collaborative and supportive environment.",
    "I am satisfied with the leadership and direction my leader provides.",
    "I feel that my leader values my contributions.",
    "My leader supports my personal growth within the team.",
    "Our team consistently meets or exceeds performance targets.",
    "Our team is adaptable and performs well in changing conditions.",
    "Our team’s achievements are recognized within the organization."
]


# Scale descriptors
scale_descriptors = [
    "1 - Not at all",
    "2 - Once in a while",
    "3 - Sometimes",
    "4 - Fairly often",
    "5 - Frequently, if not always"
]

# Function to calculate average scores
def calculate_average(scores):
    return sum(scores) / len(scores)

# Streamlit UI
st.title("Leadership Questionnaire")

# Collect responses for each section
def collect_responses(questions):
    responses = {}
    for index, question in enumerate(questions, start=1):
        st.write(f"{index}. {question}")
        selected_value = st.radio(
            label=f"{index}. {question}",
            options=scale_descriptors,
            index=2,  # Default to the middle option
            key=question,
            label_visibility='collapsed',
            # horizontal=True
        )
        responses[question] = scale_descriptors.index(selected_value) + 1
    return responses

# Get responses for each section
st.title('Transformational Leadership')
transformational_responses = collect_responses(transformational_questions)
st.title('Transactional Leadership')
transactional_responses = collect_responses(transactional_questions)
st.title('Laissez Faire Leadership')
laissez_faire_responses = collect_responses(laissez_faire_questions)
st.title('Team Effectiveness')
team_effectiveness_responses = collect_responses(team_effectiveness_questions)

# Calculate scores
transformational_score = calculate_average(list(transformational_responses.values()))
transactional_score = calculate_average(list(transactional_responses.values()))
laissez_faire_score = calculate_average(list(laissez_faire_responses.values()))
team_effectiveness_score = calculate_average(list(team_effectiveness_responses.values()))

# Display results
if st.button("Calculate Results"):
    st.header("Results")
    st.write(f"**Transformational Leadership Score:** {transformational_score:.2f}")
    st.write(f"**Transactional Leadership Score:** {transactional_score:.2f}")
    st.write(f"**Laissez-Faire Leadership Score:** {laissez_faire_score:.2f}")
    st.write(f"**Team and Leader Effectiveness Score:** {team_effectiveness_score:.2f}")