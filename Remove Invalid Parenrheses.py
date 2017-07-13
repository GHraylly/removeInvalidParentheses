class Solution(object):
    import string
    def deletePairingParesFromFront(self ,sslist):
        """
        :param sslist: list
        :return: list, baleen
        """
        changeMark = False
        slist = list(sslist)
        i = 0
        for character in slist:
            if character == '(':
                j = i + 1
                if j <= len(slist)-1:
                    while 1:
                        if slist[j] == ')':
                            slist[i] = ''
                            slist[j] = ''
                            changeMark = True
                            break
                        j += 1
                        if j >= len(slist):
                            break
            i += 1
        return slist, changeMark

    def deletePairingParesFromBehind(self, sslist):
        #从后向前，为每一个’（‘配对最远的‘）’
        """
        delete Pairing Parentheses between p1 and p2
        :param sslist: list
        :return: list, baleen
        """
        changeMark = False
        slist = list(sslist)
        i = len(slist)-1
        for character in slist[::-1]:#倒序character
            if character == '(':
                j = len(slist)-1
                if j >= -1:
                    while j >= i:
                        if slist[j] == ')':
                            slist[i] = ''
                            slist[j] = ''
                            changeMark = True
                            break
                        j -= 1
                        if j <= -1:
                            break
            i -= 1
        return slist, changeMark

    def findErrParentheses(self,sslist):
        """
        delete incorrect Parenthese in the list
        :type sslist: list
        :rtype errNum： list
        """
        slist = list(sslist)
        deleCorrList = []

        pairList, changeMark = self.deletePairingParesFromBehind(slist)
        while changeMark:
            pairList, changeMark = self.deletePairingParesFromBehind(pairList)
        for err in deleCorrList:
            if pairList == err:
                break
        else:
            deleCorrList.append(pairList)

        pairList, changeMark = self.deletePairingParesFromFront(slist)
        while changeMark:
            pairList, changeMark = self.deletePairingParesFromFront(pairList)
        if not deleCorrList:
            deleCorrList.append(pairList)
        for err in deleCorrList:
            if pairList == err:
                break
        else:
            deleCorrList.append(pairList)

        # errList = [[] for count in range(len(deleCorrList))]
        # i = 0
        # for cor in deleCorrList:
        #     for j in range(len(cor)):
        #         if cor[j] != slist[j]:
        #             errList[i].append(j)
        #     i += 1

        errList = [[] for count in range(len(deleCorrList))]
        i = 0
        for cor in deleCorrList:
            for j in range(len(cor)):
                if cor[j] == '(' or cor[j] == ')':
                    errList[i].append(j)
            i += 1

        return errList

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        slist = list(s)
        errList = self.findErrParentheses(list(slist))
        rList = []
        #errNote = [[] for count in range(len(errList))]#the same lenth with
        #
        # i = 0
        # for err in errList:
        #     j = 0
        #     for stri in err:
        #         if stri == '(' or stri == ')':
        #             errNote[i].append(j)
        #         j += 1
        #     i += 1
        for err in errList:
            rListI = list(slist)
            p = 0
            for j in err:
                rListI.pop(j-p)
                p += 1
            rListI = ''.join(rListI)
            rList.append(rListI)
        returnList = list(set(rList))
        returnList.sort(key=rList.index)
        return returnList


test = '(((k()(('
T = Solution()
print (T.removeInvalidParentheses(test))
