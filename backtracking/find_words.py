# TODO not working

def find_words(board: list[list[str]], words: list[str]) -> list[str]:

    class Trie:
        def __init__(self):
            self.children: dict[str, Trie] = {}
            self.is_word = False


        def insert(self, word: str):
            curr = self
            for letter in word:
                if letter not in curr.children:
                    curr.children[letter] = Trie()
                curr = curr.children[letter]
            curr.is_word = True


        def search(self, word: str, search_only_for_prefix = False) -> bool:
            curr = self
            for letter in word:
                if letter not in curr.children:
                    return False
                curr = curr.children[letter]
            return search_only_for_prefix or curr.is_word


    def backtrack(result: list[str], trie: Trie, used: set[tuple[int, int]],
                  curr_word: str, curr: tuple[int, int]):
        if trie.search(curr_word) and curr_word not in result:
            result.append(curr_word)
        if trie.search(curr_word, True):
            curr_i, curr_j = curr
            for (i, j) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                if 0 <= curr_i + i < len(board) and 0 <= curr_j + j < len(board[0]) \
                    and (curr_i + i, curr_j + j) not in used:
                    curr_word += board[curr_i + i][curr_j + j]
                    used.add((curr_i + i, curr_j + j))
                    backtrack(result, trie, used, curr_word, (curr_i + i, curr_j + j))
                    curr_word = curr_word[:-1]
                    used.remove((curr_i + i, curr_j + j))


    trie = Trie()
    for word in words:
        trie.insert(word)
    result = []
    for i, row in enumerate(board):
        for j, letter in enumerate(row):
            if len(result) >= len(words):
                break
            if letter in trie.children:
                backtrack(result, trie, set([(i, j)]), letter, (i, j))
    return result


def main():
    tests = [
        ([["a"]], ["a"]),
        ([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
         ["oath","pea","eat","rain"]),
        ([["a","b"],["c","d"]], ["abcb"]),
        ([["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]],
         ["oa","oaa"]),
        ([["a","b","c"],["a","e","d"],["a","f","g"]],
         ["eaafgdcba","eaabcdgfa"]),
        ([["a","a","a","a","a","a","a","a","a","a","a","a"],
          ["a","a","a","a","a","a","a","a","a","a","a","a"],
          ["a","a","a","a","a","a","a","a","a","a","a","a"],
          ["a","a","a","a","a","a","a","a","a","a","a","a"],
          ["a","a","a","a","a","a","a","a","a","a","a","a"],
          ["a","a","a","a","a","a","a","a","a","a","a","a"],
          ["a","a","a","a","a","a","a","a","a","a","a","a"],
          ["a","a","a","a","a","a","a","a","a","a","a","a"],
          ["a","a","a","a","a","a","a","a","a","a","a","a"],
          ["a","a","a","a","a","a","a","a","a","a","a","a"],
          ["a","a","a","a","a","a","a","a","a","a","a","a"],
          ["a","a","a","a","a","a","a","a","a","a","a","a"]],
         ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]),
        ([["a","a"]],
         ["aaa"]),
        ([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
         ["oath","pea","eat","rain","oathi","oathk","oathf","oate","oathii","oathfi","oathfii"]),
        ([["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"]],
         ["aababababa","abbabababa","acbabababa","adbabababa","aebabababa","afbabababa","agbabababa","ahbabababa","aibabababa","ajbabababa","akbabababa","albabababa","ambabababa","anbabababa","aobabababa","apbabababa","aqbabababa","arbabababa","asbabababa","atbabababa","aubabababa","avbabababa","awbabababa","axbabababa","aybabababa","azbabababa","bababababa","bbbabababa","bcbabababa","bdbabababa","bebabababa","bfbabababa","bgbabababa","bhbabababa","bibabababa","bjbabababa","bkbabababa","blbabababa","bmbabababa","bnbabababa","bobabababa","bpbabababa","bqbabababa","brbabababa","bsbabababa","btbabababa","bubabababa","bvbabababa","bwbabababa","bxbabababa","bybabababa","bzbabababa","cababababa","cbbabababa","ccbabababa","cdbabababa","cebabababa","cfbabababa","cgbabababa","chbabababa","cibabababa","cjbabababa","ckbabababa","clbabababa","cmbabababa","cnbabababa","cobabababa","cpbabababa","cqbabababa","crbabababa","csbabababa","ctbabababa","cubabababa","cvbabababa","cwbabababa","cxbabababa","cybabababa","czbabababa","dababababa","dbbabababa","dcbabababa","ddbabababa","debabababa","dfbabababa","dgbabababa","dhbabababa","dibabababa","djbabababa","dkbabababa","dlbabababa","dmbabababa","dnbabababa","dobabababa","dpbabababa","dqbabababa","drbabababa","dsbabababa","dtbabababa","dubabababa","dvbabababa","dwbabababa","dxbabababa","dybabababa","dzbabababa","eababababa","ebbabababa","ecbabababa","edbabababa","eebabababa","efbabababa","egbabababa","ehbabababa","eibabababa","ejbabababa","ekbabababa","elbabababa","embabababa","enbabababa","eobabababa","epbabababa","eqbabababa","erbabababa","esbabababa","etbabababa","eubabababa","evbabababa","ewbabababa","exbabababa","eybabababa","ezbabababa","fababababa","fbbabababa","fcbabababa","fdbabababa","febabababa","ffbabababa","fgbabababa","fhbabababa","fibabababa","fjbabababa","fkbabababa","flbabababa","fmbabababa","fnbabababa","fobabababa","fpbabababa","fqbabababa","frbabababa","fsbabababa","ftbabababa","fubabababa","fvbabababa","fwbabababa","fxbabababa","fybabababa","fzbabababa","gababababa","gbbabababa","gcbabababa","gdbabababa","gebabababa","gfbabababa","ggbabababa","ghbabababa","gibabababa","gjbabababa","gkbabababa","glbabababa","gmbabababa","gnbabababa","gobabababa","gpbabababa","gqbabababa","grbabababa","gsbabababa","gtbabababa","gubabababa","gvbabababa","gwbabababa","gxbabababa","gybabababa","gzbabababa","hababababa","hbbabababa","hcbabababa","hdbabababa","hebabababa","hfbabababa","hgbabababa","hhbabababa","hibabababa","hjbabababa","hkbabababa","hlbabababa","hmbabababa","hnbabababa","hobabababa","hpbabababa","hqbabababa","hrbabababa","hsbabababa","htbabababa","hubabababa","hvbabababa","hwbabababa","hxbabababa","hybabababa","hzbabababa","iababababa","ibbabababa","icbabababa","idbabababa","iebabababa","ifbabababa","igbabababa","ihbabababa","iibabababa","ijbabababa","ikbabababa","ilbabababa","imbabababa","inbabababa","iobabababa","ipbabababa","iqbabababa","irbabababa","isbabababa","itbabababa","iubabababa","ivbabababa","iwbabababa","ixbabababa","iybabababa","izbabababa","jababababa","jbbabababa","jcbabababa","jdbabababa","jebabababa","jfbabababa","jgbabababa","jhbabababa","jibabababa","jjbabababa","jkbabababa","jlbabababa","jmbabababa","jnbabababa","jobabababa","jpbabababa","jqbabababa","jrbabababa","jsbabababa","jtbabababa","jubabababa","jvbabababa","jwbabababa","jxbabababa","jybabababa","jzbabababa","kababababa","kbbabababa","kcbabababa","kdbabababa","kebabababa","kfbabababa","kgbabababa","khbabababa","kibabababa","kjbabababa","kkbabababa","klbabababa","kmbabababa","knbabababa","kobabababa","kpbabababa","kqbabababa","krbabababa","ksbabababa","ktbabababa","kubabababa","kvbabababa","kwbabababa","kxbabababa","kybabababa","kzbabababa","lababababa","lbbabababa","lcbabababa","ldbabababa","lebabababa","lfbabababa","lgbabababa","lhbabababa","libabababa","ljbabababa","lkbabababa","llbabababa","lmbabababa","lnbabababa","lobabababa","lpbabababa","lqbabababa","lrbabababa","lsbabababa","ltbabababa","lubabababa","lvbabababa","lwbabababa","lxbabababa","lybabababa","lzbabababa","mababababa","mbbabababa","mcbabababa","mdbabababa","mebabababa","mfbabababa","mgbabababa","mhbabababa","mibabababa","mjbabababa","mkbabababa","mlbabababa","mmbabababa","mnbabababa","mobabababa","mpbabababa","mqbabababa","mrbabababa","msbabababa","mtbabababa","mubabababa","mvbabababa","mwbabababa","mxbabababa","mybabababa","mzbabababa","nababababa","nbbabababa","ncbabababa","ndbabababa","nebabababa","nfbabababa","ngbabababa","nhbabababa","nibabababa","njbabababa","nkbabababa","nlbabababa","nmbabababa","nnbabababa","nobabababa","npbabababa","nqbabababa","nrbabababa","nsbabababa","ntbabababa","nubabababa","nvbabababa","nwbabababa","nxbabababa","nybabababa","nzbabababa","oababababa","obbabababa","ocbabababa","odbabababa","oebabababa","ofbabababa","ogbabababa","ohbabababa","oibabababa","ojbabababa","okbabababa","olbabababa","ombabababa","onbabababa","oobabababa","opbabababa","oqbabababa","orbabababa","osbabababa","otbabababa","oubabababa","ovbabababa","owbabababa","oxbabababa","oybabababa","ozbabababa","pababababa","pbbabababa","pcbabababa","pdbabababa","pebabababa","pfbabababa","pgbabababa","phbabababa","pibabababa","pjbabababa","pkbabababa","plbabababa","pmbabababa","pnbabababa","pobabababa","ppbabababa","pqbabababa","prbabababa","psbabababa","ptbabababa","pubabababa","pvbabababa","pwbabababa","pxbabababa","pybabababa","pzbabababa","qababababa","qbbabababa","qcbabababa","qdbabababa","qebabababa","qfbabababa","qgbabababa","qhbabababa","qibabababa","qjbabababa","qkbabababa","qlbabababa","qmbabababa","qnbabababa","qobabababa","qpbabababa","qqbabababa","qrbabababa","qsbabababa","qtbabababa","qubabababa","qvbabababa","qwbabababa","qxbabababa","qybabababa","qzbabababa","rababababa","rbbabababa","rcbabababa","rdbabababa","rebabababa","rfbabababa","rgbabababa","rhbabababa","ribabababa","rjbabababa","rkbabababa","rlbabababa","rmbabababa","rnbabababa","robabababa","rpbabababa","rqbabababa","rrbabababa","rsbabababa","rtbabababa","rubabababa","rvbabababa","rwbabababa","rxbabababa","rybabababa","rzbabababa","sababababa","sbbabababa","scbabababa","sdbabababa","sebabababa","sfbabababa","sgbabababa","shbabababa","sibabababa","sjbabababa","skbabababa","slbabababa","smbabababa","snbabababa","sobabababa","spbabababa","sqbabababa","srbabababa","ssbabababa","stbabababa","subabababa","svbabababa","swbabababa","sxbabababa","sybabababa","szbabababa","tababababa","tbbabababa","tcbabababa","tdbabababa","tebabababa","tfbabababa","tgbabababa","thbabababa","tibabababa","tjbabababa","tkbabababa","tlbabababa","tmbabababa","tnbabababa","tobabababa","tpbabababa","tqbabababa","trbabababa","tsbabababa","ttbabababa","tubabababa","tvbabababa","twbabababa","txbabababa","tybabababa","tzbabababa","uababababa","ubbabababa","ucbabababa","udbabababa","uebabababa","ufbabababa","ugbabababa","uhbabababa","uibabababa","ujbabababa","ukbabababa","ulbabababa","umbabababa","unbabababa","uobabababa","upbabababa","uqbabababa","urbabababa","usbabababa","utbabababa","uubabababa","uvbabababa","uwbabababa","uxbabababa","uybabababa","uzbabababa","vababababa","vbbabababa","vcbabababa","vdbabababa","vebabababa","vfbabababa","vgbabababa","vhbabababa","vibabababa","vjbabababa","vkbabababa","vlbabababa","vmbabababa","vnbabababa","vobabababa","vpbabababa","vqbabababa","vrbabababa","vsbabababa","vtbabababa","vubabababa","vvbabababa","vwbabababa","vxbabababa","vybabababa","vzbabababa","wababababa","wbbabababa","wcbabababa","wdbabababa","webabababa","wfbabababa","wgbabababa","whbabababa","wibabababa","wjbabababa","wkbabababa","wlbabababa","wmbabababa","wnbabababa","wobabababa","wpbabababa","wqbabababa","wrbabababa","wsbabababa","wtbabababa","wubabababa","wvbabababa","wwbabababa","wxbabababa","wybabababa","wzbabababa","xababababa","xbbabababa","xcbabababa","xdbabababa","xebabababa","xfbabababa","xgbabababa","xhbabababa","xibabababa","xjbabababa","xkbabababa","xlbabababa","xmbabababa","xnbabababa","xobabababa","xpbabababa","xqbabababa","xrbabababa","xsbabababa","xtbabababa","xubabababa","xvbabababa","xwbabababa","xxbabababa","xybabababa","xzbabababa","yababababa","ybbabababa","ycbabababa","ydbabababa","yebabababa","yfbabababa","ygbabababa","yhbabababa","yibabababa","yjbabababa","ykbabababa","ylbabababa","ymbabababa","ynbabababa","yobabababa","ypbabababa","yqbabababa","yrbabababa","ysbabababa","ytbabababa","yubabababa","yvbabababa","ywbabababa","yxbabababa","yybabababa","yzbabababa","zababababa","zbbabababa","zcbabababa","zdbabababa","zebabababa","zfbabababa","zgbabababa","zhbabababa","zibabababa","zjbabababa","zkbabababa","zlbabababa","zmbabababa","znbabababa","zobabababa","zpbabababa","zqbabababa","zrbabababa","zsbabababa","ztbabababa","zubabababa","zvbabababa","zwbabababa","zxbabababa","zybabababa","zzbabababa"])
    ]
    expected = [
        ["a"],
        ["oath", "eat"],
        [],
        ["oa","oaa"],
        ["eaafgdcba","eaabcdgfa"],
        ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"],
        [],
        ["oath","oathk","oathf","oathfi","oathfii","oathi","oathii","oate","eat"],
        ['bababababa']
    ]
    for test, expected in zip(tests, expected):
        board, words = test
        assert find_words(board, words) == expected

if __name__ == "__main__":
    main()
