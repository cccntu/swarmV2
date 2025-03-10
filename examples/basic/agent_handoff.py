from swarm import Swarm, Agent

client = Swarm()

english_agent = Agent(
    name="English Agent",
    instructions="You only speak English.",
)

spanish_agent = Agent(
    name="Spanish Agent",
    instructions="You only speak Spanish.",
)


def transfer_to_spanish_agent():
    """Transfer spanish speaking users immediately."""
    return spanish_agent

def transfer_to_english_agent():
    """Transfer english speaking users immediately."""
    return english_agent


english_agent.functions.append(transfer_to_spanish_agent)
spanish_agent.functions.append(transfer_to_english_agent)

messages = []
agent = english_agent
while True:
    user_input = input("> ")
    messages.append({"role": "user", "content": user_input})

    response = client.run(agent=agent, messages=messages, debug=True)
    print("response:", response.messages[-1]["content"])
    agent = response.agent
    messages.extend(response.messages)
