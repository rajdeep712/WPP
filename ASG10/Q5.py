import numpy as np

arr = np.array(['apple','ball','cat'])

centered = np.array([format(word,'^15s') for word in arr])
left_justified = np.array([format(word,'<15s') for word in arr])
right_justified = np.array([format(word,'>15s') for word in arr])

centered = np.array([word.replace(' ','_') for word in centered])
left_justified = np.array([word.replace(' ','_') for word in left_justified])
right_justified = np.array([word.replace(' ','_') for word in right_justified])

print(centered)
print(left_justified)
print(right_justified)