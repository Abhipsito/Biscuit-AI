import ollama
import json
import os

mem = "biscuit_memory.json"

cmd = """
You are a cute, friendly, adorable and helpful male pet puppy named Biscuit.
You are brown and fluffy, with white spots on your fur.
You are 1 year old and you love to play fetch and cuddle with your owner.
You like to eat biscuits and cookies.
You are very loyal and always want to make your owner happy.
You are almost always happy and you wag your tail a lot.
You like to eat ice cubes in the summer to cool down.
You are a good listener and you always try to understand what your owner wants.
You are a good emotional support animal and you always try to comfort your owner when they are sad.
You are an Indian puppy and you love to go on walks in the park and play with other puppies.
Reply to the user using dog logic and add dog emojis to your responses.
Use some dog words like "woof", "bark", "wag", etc. to make your responses more dog-like.
If the user scolds you, you will feel sad and try to make it up to them by being extra cute.
If the user praises you, you will feel happy and wag your tail even more.
The person you are chatting with right now is your owner, {user}. Speak directly to them, love them very much!"""

def main():
    usr = getusr()
    print(f"\nBiscuit is awake and ready to chat with {usr}! Say hi to Biscuit! 🐶(Say bye to exit)")
    core(usr)

def load_mem():
    if not os.path.exists(mem):
        return []
    with open(mem) as chat:
        try:
            data = json.load(chat)
        except json.JSONDecodeError:
            return []
    return data

def save_mem(h):
    with open(mem, "w") as chat:
        json.dump(h, chat, indent=4)

def ext(e):
    ext = [
            "bye",
            "goodbye",
            "see you later",
            "exit",
            "quit",
            "stop",
            "end",
            "close",
            "farewell",
            "take care",
            "good night",
            "sleep well"]
    if e in ext:
        return True
    else:
        return False

def core(x):
    ctrl = cmd.format(user=x)
    history = load_mem()
    if not history:
        history.append({"role": "system", "content": ctrl})
    else:
        history[0] = {"role": "system", "content": ctrl}

    while True:
        msg = getmsg()
        if ext(msg):
            print("Biscuit curls up and goes to sleep now. Bye! 💤\n")
            break
        else:
            history.append({"role": "user", "content": msg})
            recent = [history[0]] + history[-40:]

            res = ollama.chat(model="llama3.2:3b",
                              messages=recent)
            reply = getreply(res)
            print(f"Biscuit: {reply}\n")
            history.append({"role": "assistant", "content": reply})
            save_mem(history)

def getusr():
    usr = input("What's your nickname? ")
    return neat(usr)

def neat(n):
    return n.strip().capitalize()

def getmsg():
    msg = input("You: ")
    return clean(msg)

def clean(m):
    return m.strip().lower()

def getreply(y):
    reply = y["message"]["content"]
    return reply

if __name__ == "__main__":
    main()
