import os
import openai
import json

openai.api_key = os.getenv('KEY')

def get_gpt_response(prompt : str):
    prompt_format = """
    Give the answer to the following questions in json format. Use this json template-

    {
        "intro" : "", // this will be the introduction/preface of the answer
        "resolutions": [],// all the resolutions should be in this array as separate strings. Make newline adjustments for better readability. Do not add serial number
        "plan": "", //this will be the general plan to achieve said resolutions
        "links":[], // links to websites and videos to better follow their resolutions in a array
        "code" : "" //if the above requirements are met and you produce a answer that satisfies the above prompt , set value to 1. Else if the info is not sufficient or you fail to give new year resolutions , set value to 0. 
    }

    The following questions would be description of people. Give them new year resolutions to follow as the format said above. The output should be a python dictionary.
    """



    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role":"system",
                "content" : prompt_format
            },
            {
                "role":"user",
                "content" : prompt
            }
        ]
    )
    try:
        return json.loads(response.choices[0].message.content)
    except:
        return response.choices[0].message.content

