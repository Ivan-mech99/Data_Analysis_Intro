from collections import deque
import string


class TrieIterator:

    def __init__(self, base):
        self.alphabet = "{}{}{}".format(
            string.digits,
            string.ascii_uppercase,
            string.ascii_lowercase)
        self.obj = deque([base])
        if base.temp is None:
            self.data = deque([""])
        else:
            self.data = deque([base.temp])

    def __iter__(self):
        return self

    def __next__(self):
        while len(self.obj) != 0:
            node1 = self.obj.popleft()
            data1 = self.data.popleft()
            for symbol in self.alphabet:
                if symbol in node1.next_nodes:
                    self.obj.append(node1.next_nodes[symbol])
                    self.data.append(data1+symbol)
            if node1.key:
                return data1
        raise StopIteration


class Node:

    def __init__(self, prev_node=None, key=False, symbol=""):
        self.prev_node = prev_node
        self.key = key
        self.symbol = symbol
        self.next_nodes = dict()
        self.temp = None

    def add_next_node(self, node1):
        self.next_nodes[node1.symbol] = node1


class Trie:

    def __init__(self):
        self.root = Node()
        self.elem_amount = 0

    def __contains__(self, key):
        empt = dict()
        cur_node = self.root
        cur_ind = 0
        while True:
            if cur_ind+1 != len(key):
                if key[cur_ind] in cur_node.next_nodes:
                    cur_node = cur_node.next_nodes[key[cur_ind]]
                    cur_ind = cur_ind+1
                else:
                    return False
            else:
                if cur_node.next_nodes != empt:
                    cur_node = cur_node.next_nodes[key[cur_ind]]
                    return cur_node.key
                else:
                    return False

    def add(self, key):
        cur_node = self.root
        cur_ind = 0
        work = True
        while work:
            if cur_ind+1 != len(key):
                if key[cur_ind] in cur_node.next_nodes:
                    cur_node = cur_node.next_nodes[key[cur_ind]]
                    cur_ind = cur_ind+1
                else:
                    temp1 = Node(prev_node=cur_node, symbol=key[cur_ind])
                    cur_node.next_nodes[key[cur_ind]] = temp1
                    cur_node = cur_node.next_nodes[key[cur_ind]]
                    cur_ind = cur_ind+1
            else:
                if key[cur_ind] in cur_node.next_nodes:
                    cur_node = cur_node.next_nodes[key[cur_ind]]
                    work = False
                    if cur_node.key is False:
                        cur_node.key = True
                        self.elem_amount = self.elem_amount+1
                else:
                    temp1 = Node(prev_node=cur_node, symbol=key[cur_ind])
                    cur_node.next_nodes[key[cur_ind]] = temp1
                    cur_node = cur_node.next_nodes[key[cur_ind]]
                    cur_node.key = True
                    work = False
                    self.elem_amount = self.elem_amount+1

    def pop(self, key):
        empt = dict()
        cur_node = self.root
        cur_ind = 0
        work = True
        while work:
            if cur_ind+1 != len(key):
                if key[cur_ind] in cur_node.next_nodes:
                    cur_node = cur_node.next_nodes[key[cur_ind]]
                    cur_ind = cur_ind+1
                else:
                    work = False
                    res = False
            else:
                cur_node = cur_node.next_nodes[key[cur_ind]]
                res = cur_node.key
                work = False
        if res is False:
            raise KeyError(key)
        cur_node.key = False
        while True:
            if cur_node == self.root or cur_node.next_nodes != empt:
                break
            temp = cur_node.symbol
            cur_node = cur_node.prev_node
            cur_node.next_nodes.pop(temp)
        self.elem_amount = self.elem_amount-1

    def __len__(self):
        return self.elem_amount

    def __iter__(self):
        return TrieIterator(self.root)

    def needed_prefix(self, prefix):
        cur_node = self.root
        nd_prefix = ""
        for symb in prefix:
            work = False
            for symb1, nextn in cur_node.next_nodes.items():
                if symb == symb1:
                    cur_node = nextn
                    nd_prefix = nd_prefix + symb
                    work = True
                    break

            if not work:
                break
        cur_node.temp = nd_prefix
        return nd_prefix, cur_node

    def starts_with(self, prefix):
        nd_prefix, node1 = self.needed_prefix(prefix)
        if len(nd_prefix) != len(prefix):
            return TrieIterator(Node())
        return TrieIterator(node1)
