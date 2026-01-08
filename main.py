from agent import LlmAgent

if __name__ == "__main__":
  agent = LlmAgent()
  reply = agent.handle("정민기", "날씨는 어때?")
  print("응답:", reply)