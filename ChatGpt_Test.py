from openai import OpenAI
import os
apikey = '' # Здесь хранится секретный API ключ.
client = OpenAI(
    api_key=apikey,
)
def get_chatgpt_response(prompt, rules):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ты рассказчик."},  # Контекст или роль AI
            {"role": "system", "content": rules},  # Правила и контекст
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    #print(os.getcwd())
    with open('C:\\Users\\User\\Documents\\Unreal Projects\\MyProject\\Content\\Core\\Scripts\\user_prompt.txt', 'r') as file:
        user_prompt = file.read()
    
    lore_rules = """
    1. Мир игры называется Элония.
    2. Главный герой - Луна, обладающая уникальным даром общения c природой.
    3. Есть древний артефакт - Кристалл Света, способный победить тьму.
    4. Злодей - эльбский маг по имени Аремлон.
    5. B финале битва co злыми силами и победа Луны.
    """
    
    response = get_chatgpt_response(user_prompt, lore_rules)
    
    with open('C:\\Users\\User\\Documents\\Unreal Projects\\MyProject\\Content\\Core\\Scripts\\response.txt', 'w') as file:
        file.write(response)