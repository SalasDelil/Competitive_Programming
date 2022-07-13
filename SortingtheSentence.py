class Solution(object):
    def sortSentence(self, s):
        sent = s.split(" ")
        new_sent = [""]*len(sent)

        for element in sent:
            sub_ele = []
            word = ""
            for ele in element:
                sub_ele.append(ele)

            k = int(sub_ele[-1])
            sub_ele.pop(-1)
            for alp in sub_ele:
                word += alp
            new_sent[k - 1] = word
            
        sentence = ""
        n = len(new_sent)
        for i in range(n):
            if i < n - 1:
                sentence += new_sent[i] + " "
            else:
                sentence += new_sent[i]

        return sentence
        
