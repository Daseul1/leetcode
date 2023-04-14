class MyStack:

    def __init__(self):
        self.stack = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1] # -1 : "리스트 마지막 요솟값
        
    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True # 소문자로 작성하게 되면 boolen 값으로 읽히지 않음 주의!!!!!
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()