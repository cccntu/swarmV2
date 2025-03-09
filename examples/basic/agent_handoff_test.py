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

if __name__ == "__main__":
    messages = []
    agent = english_agent
    inputs = [
        'Hola', # triggers handoff to spanish agent
        'tell me a english joke', # triggers handoff back to english agent
    ]
    for input in inputs:
        messages.append({"role": "user", "content": input})
        response = client.run(agent=agent, messages=messages, debug=True)
        print('Input:', input)
        print("response:", response.messages[-1]["content"])
        agent = response.agent
        messages.extend(response.messages)
