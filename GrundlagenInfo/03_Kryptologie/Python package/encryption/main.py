from friedmann import *
from vigenere import *
plt.style.use('ggplot')

if __name__ == '__main__':
    file = open('text.txt','r')
    text = file.read()
    # optionally shorten the text to show artefacts
    # text = text[:100]
    print(len(text))
    text = vigenere(text, "KEY")
    n=range(1,10)
    fc=[]
    for i in n:
        fc.append(friedmann_slice(text,i))
    print(fc)

    plt.plot(n, fc, 'o')
    # optionally save the figure
    # plt.savefig('more_data.pdf',bbox_inches='tight', pad_inches=0)  
    plt.show()
    

    
    