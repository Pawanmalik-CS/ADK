# from google.adk.agents.llm_agent import Agent

# root_agent = Agent(
#     model='gemini-2.5-flash',
#     name='root_agent',
#     description='A helpful assistant for user questions.',
#     instruction='Answer user questions to the best of your knowledge',
# )



from google.adk.agents.llm_agent import Agent


root_agent = Agent(

    model='gemini-2.5-flash',

    name='math_tutor_agent',

    description='Helps students learn algebra by guiding them through problemsolving steps.',

    instruction='You are a patient math tutor. Help students with algebra problems.'

)
3
## trasnforming the basic agent from module 1 to specific agent for tutoring math. We have changed the name, description and instruction to make it more specific to the task of tutoring math.
