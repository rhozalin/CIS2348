# Name-Rhozalin Nath
# PS ID: 2050395

def selection_sort_descend_trace(l):
    updated_list = []
    for i in l:
        updated_list.append(int(i))

    for i in range(len(updated_list) - 1):
        temp = i

        for j in range(len(updated_list) - 1, i, -1):
            if updated_list[j] > updated_list[temp]:
                temp = j

        if temp != i:
            updated_list[i], updated_list[temp] = updated_list[temp], updated_list[i]

        for x in updated_list:
            print(x, end=" ")
        print()

if __name__ == "__main__":
    l = input().split()
    selection_sort_descend_trace(l)
