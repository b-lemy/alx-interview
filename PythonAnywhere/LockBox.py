#!/usr/bin/python3
''' lockbox module '''


def canUnlockAll(boxes):
    '''
        CanUnockAll
        ([boxes]): a list of list
    '''

    # initialize a list of unlocked boxes
    unlocked = [False] * len(boxes)
    print(unlocked)
    # set the first box to true
    unlocked[0] = True
    print(unlocked)
    # iterate over the boxes
    for index, box in enumerate(boxes):
        # check if the box is unlocked
        print(index, box)
        if unlocked[index]:
            print(unlocked[index])
            # get the keys in the box
            for index, key in enumerate(box):
                print(index, key, box)
                # set the box with a found key to open
                if key < len(unlocked):
                    unlocked[key] = True
                    print(unlocked)
                    print(key)
                    # get the keys at the box that has been opened
                    # set the boxes with the keys to be open
                    for i in boxes[key]:
                        print(i)
                        print(boxes[key])
                        print('----')
                        unlocked[i] = True
    return all(unlocked)


boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

# boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
# print(canUnlockAll(boxes))
#
# boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
# print(canUnlockAll(boxes))