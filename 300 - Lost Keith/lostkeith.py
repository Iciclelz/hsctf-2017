import sys

#flag: odejhsjkf_q_yuiwahekjgo_piqiuerifwg_ashjdfjaiu_weyg

class lost_keith_node:
    def __init__(self, value):
        #self.unknown1  57005
        self.left = None
        # self.unknown2  48879
        # self.unknown3  4
        # self.unknown4  47789
        self.right = None
        # self.unknown5  61453
        self.value = value
        #self.unknown6 375

class lost_keith_tree:
    def __init__(self):
        self.instruction = '72662672667266662672666762726666267266667266622726626227622726626227626676262272666627' \
                           '62672662627266672667266667266662672666277266262276222726666276227266662762622726676226' \
                           '72666627266622762672666272662622726626276272666726666267266267266622726666267266262726' \
                           '66627626227266262276267266762667266627'

        self.data = "o4zs7eh83wydagkijvqux_fr9lbp2"
        self.root = None

        self.i = list()

        temp = ''
        for x in range(len(self.instruction)):
            temp += self.instruction[x]
            if self.instruction[x] == '7':
                self.i.append(temp)
                temp = ''

        for x in range(len(self.data)):
            self.root = self.retrieve(self.root, self.data[x])

    def retrieve(self, node, m):
        if node is not None:
            if node.value >= m:
                node.left = self.retrieve(node.left, m)
                return node
            else:
                node.right = self.retrieve(node.right, m)
                return node
        else:
            node = lost_keith_node(0)

            node.left = None
            node.right = None
            node.value = m

            return node

    def solve(self):
        print(self.i)
        sys.stdout.write("\nflag: ")
        for x in range(len(self.i)):
            current_node = self.root
            for y in range(len(self.i[x])):
                if self.i[x][y] == '7':
                    sys.stdout.write("%c" % current_node.value)
                    current_node = self.root
                elif self.i[x][y] == '6':
                    current_node = current_node.right
                elif self.i[x][y] == '2':
                    current_node = current_node.left
                else:
                    print('error')

tree = lost_keith_tree()
tree.solve()
