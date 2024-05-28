import string

st = input('Enter hashtag string ')
st = st.lower()

st = list(st)

for i in st:
    if i in string.punctuation:
        st.remove(i)

res = ''.join(''.join(st).title().split())


print('#'+res)
