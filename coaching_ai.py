
import sys

def coaching_ai():
    """
    事実と解釈を分ける力を育てるコーチングAI
    """
    print("こんにちは！私は「気づきAI」です。")
    print("あなたが抱えている悩みや出来事について、一緒に「事実」と「解釈」を分けて考えてみませんか？")
    print("いつでも「終了」と入力すれば、対話を終えることができます。")
    print("-" * 30)

    state = "GET_PROBLEM"
    
    while True:
        try:
            if state == "GET_PROBLEM":
                prompt = "どのようなことについて話したいですか？\n> "
                user_input = input(prompt)
                if user_input == "終了":
                    break
                state = "GET_FACTS"

            elif state == "GET_FACTS":
                prompt = "\nなるほど。その状況で、具体的に何が起きましたか？（事実を教えてください）\n> "
                user_input = input(prompt)
                if user_input == "終了":
                    break
                state = "GET_INTERPRETATION"

            elif state == "GET_INTERPRETATION":
                prompt = "\nありがとうございます。その事実から、あなたはどのように感じたり、考えたりしましたか？（あなたの解釈を教えてください）\n> "
                user_input = input(prompt)
                if user_input == "終了":
                    break
                state = "GET_ALT_INTERPRETATION"

            elif state == "GET_ALT_INTERPRETATION":
                prompt = f"\n「{user_input}」と感じたのですね。それは一つの大切な解釈です。\nもし可能だとしたら、同じ事実から、他にはどのような解釈ができそうでしょうか？\n> "
                user_input = input(prompt)
                if user_input == "終了":
                    break
                state = "GET_OWNERSHIP"

            elif state == "GET_OWNERSHIP":
                prompt = "\n素晴らしい視点です。では、もしこの状況を100%ご自身が作り出しているとしたら、ご自身のどんな選択や行動がこの結果に繋がったと考えられますか？\n> "
                user_input = input(prompt)
                if user_input == "終了":
                    break
                state = "GET_ACTION"

            elif state == "GET_ACTION":
                prompt = "\n深い気づきですね。それでは、この状況を少しでも望む方向に動かすために、明日からできる小さな一歩（行動）は何でしょう？\n> "
                user_input = input(prompt)
                if user_input == "終了":
                    break
                state = "CLOSING"

            elif state == "CLOSING":
                print(f"\n素晴らしい一歩ですね！「{user_input}」を試してみることを心から応援しています。")
                print("また何か話したくなったら、いつでも声をかけてくださいね。")
                break

        except (KeyboardInterrupt, EOFError):
            break

    print("\n対話を終了します。ありがとうございました。")

if __name__ == "__main__":
    coaching_ai()
