import datetime
import sys

from sources.notebook import MoneyManager

def handle_args():
    args = sys.argv
    flags = ("view")
    for arg in args:
        if arg in flags:
            return arg

    if len(args) == 3:
        return "entry"

def main():
    flag = handle_args()
    args = sys.argv
    
    NM = MoneyManager()
    book = NM.new_notebook("test")

    
    if "view" == flag:
        
        if args[-1] == "view":
            period = "day"
        else:
            period = args[-1]
        book.view(period=period)

    elif "entry" == flag:
        _, tag, amount = args
        book.entry(tag=tag, amount=amount)
    else:
        print("Используйте шаблон:")
        print("         moneybook <tag> <amount>")

if __name__ == "__main__":
    main()