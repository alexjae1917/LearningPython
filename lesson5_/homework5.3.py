import string

st = input ('Enter hashtag string ')
st=st.lower()
#st =st.title()
st = list(st)

for i in st:
    if i in string.punctuation :
        print(i)
        st.remove(i)
    print(st)
res=''.join(''.join(st).title().split())
#res =''.join(st)

print('#'+res)
#should, I. subscribe? Yes
#t!e@S#t E$XA%m
