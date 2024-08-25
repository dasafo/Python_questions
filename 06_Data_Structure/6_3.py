# Slice list into 3 equal chunks and reverse each chunks

sample_list = [70, 77, 83, 2, 4, 43, 7, 32, 9]

chunk_size = int(len(sample_list)/3)

start = 0
end = chunk_size

for i in range(3):
    index = slice(start, end)
    list_chunk = sample_list[index]

    print("After reversing it: ", list(reversed(list_chunk)))
    start = end
    end += chunk_size

