from langchain.prompts import PromptTemplate
from datetime import datetime

# 使用 Python f 字符串模板：
fstring_template = """Tell me a {adjective} joke about {content}"""
prompt = PromptTemplate.from_template(fstring_template)
print(prompt.format(adjective="funny", content="chickens"))
# Output: Tell me a funny joke about chickens.


# 使用 jinja2 模板：
jinja2_template = "Tell me a {{ adjective }} joke about {{ content }}"
prompt = PromptTemplate.from_template(jinja2_template, template_format="jinja2")
print(prompt.format(adjective="funny", content="chickens"))
# Output: Tell me a funny joke about chickens.


# 将函数的最终值作为prompt的一部分进行返回
prompt = PromptTemplate(
    template="Tell me a {adjective} joke about the day {date}",
    input_variables=["adjective", "date"]
)
def _get_datetime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y, %H:%M:%S")
partial_prompt = prompt.partial(date=_get_datetime)
print(partial_prompt.format(adjective="funny"))

