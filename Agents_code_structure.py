# Code Structure Template 

class IntelligentAgent:
    def __init__(self):
        # Initialize internal state if needed
        pass

    def perceive(self):
        """
        Simulates the sensor reading.
        Returns a percept (e.g., input from environment).
        """
        percept = input("Enter current percept (e.g., dirty, clean): ")
        return percept

    def decide_action(self, percept):
        """
        Agent function: maps percepts to actions.
        """
        if percept == "dirty":
            return "clean"
        else:
            return "move"

    def act(self, action):
        """
        Executes the action using actuators.
        """
        print(f"Agent performs action: {action}")

    def run(self, steps=5):
        """
        Runs the sense-think-act loop for N steps.
        """
        for _ in range(steps):
            percept = self.perceive()             # Sensors → Percept
            action = self.decide_action(percept)  # Agent Function → Action
            self.act(action)                      # Actuators
            print("-" * 30)


# Example execution
agent = IntelligentAgent()
agent.run()



# Simple Reflex Agent — Code Structure
# Responds directly to percepts using condition-action rules.

class SimpleReflexAgent:
    def __init__(self):
        pass

    def perceive(self, environment_input):
        return environment_input  # the percept

    def decide_action(self, percept):
        # Simple rule: if it's dirty, clean; otherwise, do nothing
        if percept == "dirty":
            return "clean"
        else:
            return "do nothing"

    def act(self, action):
        print(f"Agent action: {action}")


# Example usage
env = "dirty"
agent = SimpleReflexAgent()
percept = agent.perceive(env)
action = agent.decide_action(percept)
agent.act(action)


# Model-based Reflex Agent — Code Structure
# Keeps track of the world using internal state.

class ModelBasedAgent:
    def __init__(self):
        self.state = {"room": "unknown"}

    def perceive(self, environment_input):
        return environment_input

    def update_state(self, percept):
        self.state["room"] = percept

    def decide_action(self):
        if self.state["room"] == "dirty":
            return "clean"
        else:
            return "move to next room"

    def act(self, action):
        print(f"Agent action: {action}")


# Example usage
env = "dirty"
agent = ModelBasedAgent()
percept = agent.perceive(env)
agent.update_state(percept)
action = agent.decide_action()
agent.act(action)


# Goal-based Agent — Code Structure
# Uses goals to guide actions.

class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def perceive(self, percept):
        return percept

    def is_goal_achieved(self, percept):
        return percept == self.goal

    def decide_action(self, percept):
        if self.is_goal_achieved(percept):
            return "stop"
        else:
            return f"move towards {self.goal}"

    def act(self, action):
        print(f"Agent action: {action}")


# Example
env = "not at goal"
agent = GoalBasedAgent(goal="at goal")
percept = agent.perceive(env)
action = agent.decide_action(percept)
agent.act(action)


# Utility-based Agent — Code Structure
# Uses a utility function to choose the best action.    
class UtilityBasedAgent:
    def __init__(self):
        pass

    def perceive(self, options):
        return options  # list of possible states

    def utility(self, state):
        # Higher utility means better choice
        utilities = {"safe": 10, "risky": 2, "neutral": 5}
        return utilities.get(state, 0)

    def decide_action(self, options):
        best = max(options, key=self.utility)
        return f"choose {best}"

    def act(self, action):
        print(f"Agent action: {action}")


# Example
env_options = ["risky", "safe", "neutral"]
agent = UtilityBasedAgent()
percepts = agent.perceive(env_options)
action = agent.decide_action(percepts)
agent.act(action)


# Learning Agent — Code Structure
# Improves performance over time based on experience.


class LearningAgent:
    def __init__(self):
        self.knowledge = {}

    def perceive(self, percept):
        return percept

    def learn(self, percept, feedback):
        self.knowledge[percept] = feedback

    def decide_action(self, percept):
        return self.knowledge.get(percept, "explore")

    def act(self, action):
        print(f"Agent action: {action}")


# Example usage
agent = LearningAgent()
agent.learn("situation1", "action1")

percept = agent.perceive("situation1")
action = agent.decide_action(percept)
agent.act(action)
