import datetime
import sys

from sources.notebook import MoneyManager

def handle_args():
    args = sys.argv
    otions = ("view", "entry",)
    for arg in args:
        if arg in otions:
            return arg

    if len(args) == 3:
        return "entry"
    else:
        print("Используйте шаблон:")
        print("         moneybook <tag> <amount>")

def main():
    option = handle_args()
    args = sys.argv
    
    NM = MoneyManager()
    book = NM.new_notebook("test")

    
    match option:
        case "view":
            period = args[-1]
            book.view(period=period)
        
        case "entry":
            _, tag, amount = args
            book.entry(tag=tag, amount=amount)

if __name__ == "__main__":
    main()