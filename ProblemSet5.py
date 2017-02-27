from collections import Counter,defaultdict
from HeapTest import MinHeap, Node
from TreePrint import printTree, printCodes
import DFTInorder

read_in_string="the road not taken by robert frost two roads diverged in a yellow wood, and \
sorry i could not travel both and be one traveler, long i stood and looked down\
 one as far as i could to where it bent in the undergrowth; then took the other,\
  as just as fair, and having perhaps the better claim, because it was grassy \
  and wanted wear; though as for that the passing there had worn them really \
  about the same, and both that morning equally lay in leaves no step had trodden\
   black. oh, i kept the first for another day! yet knowing how way leads on to \
   way, i doubted if i should ever come back. i shall be telling this with a sigh\
    somewhere ages and ages hence: two roads diverged in a wood, and i- i took \
    the one less traveled by, and that has made all the difference."

def string2freq(read_string): # x is a string of symbols from alphabet.
    S = sorted(set(read_string)) #Can I use this?
    f = list()
    for character in S:
        f.append(read_string.count(character))
    return S, f

def huffmanEncode(S, f): # f is a vector of symbol frequencies, from above
    """
    Create a minHeap and add the nodes into it.
    """
    H = MinHeap() # H.initialize
    n = len(f)
    for i in range(n):
        new_nochild_node = Node(f[i], S[i], None, None) #No children because they are the lowest.
        H.insert(new_nochild_node) #Insert frequency, characater

    """ ### Debugging ###
    for i in range(H.currentSize):
        item = H.hList[i+1]
        print(item)

        if(item.leftNode or item.rightNode): #If there exists some right or left node.
            print(item.leftNode.char)
        else: print("NONE")

        input()
        #Now I need to assocaite old node (base of huffman) with new node per tier
    ### END DEBUGGING ### """

    root_node = None
    while(True):
        """
        Returns the lowest nodes on the tree to build the Huffman tree.
        """
        if (len(H.hList) > 2): #two items left in the tree
            i = H.delMin()
            j = H.delMin()
            k_sum = i.freq + j.freq
            new_node = Node(k_sum, -1, i, j)
            H.insert(new_node)
            #print(new_node.freq)
        else: break
    root_node = H.hList[1]
    adict = dict(printCodes(root_node,""))

    return adict


def encodeString(x, T):
    y = ""
    for ii in range(1, len(x)):
        y = y + T[x[ii]]
    return y

#
S, f = string2freq(read_in_string)
adict = huffmanEncode(S, f)

y = encodeString(read_in_string, adict)

print(y)
