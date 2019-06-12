#!/usr/bin/python2.7
# coding=utf-8
import json
import os.path
import os
import codecs
import itertools
from collections import defaultdict

def unionData(datas):
    # split json data
    unioneData = []
    combinedData = []
    for data in datas:
        # combine dict data
        for item in data:
            combinedData.append(item)

    for combData in combinedData:
        prepareData = []
        sheetName = combData['sSheetName']
        sameDataCont = 0
        for sameData in combinedData:            
            if sameData['sSheetName'] == sheetName:
                sameDataCont = sameDataCont + 1
                prepareData.append(sameData)

        if sameDataCont == 1:
            # no same data, sign the diff+num
            for comb in combData:
                comb['sType'] = "diff1"
            unioneData.append(combData)
        elif sameDataCont > 1:
            colsData = []
            num  = 1
            sTypes = []
            for prepare in prepareData:
                # identify from which file
                prepare['sType'] = "file" + str(num)
                sTypes.append(prepare['sType'])
                num = num + 1

            # get 'sType' and 'sName'
            compareData = []
            for sData in prepareData:
                # org list [{"sName":"","sType":""}]                
                aColsData = sData['aCols']
                for colsData in aColsData:
                    compDict = {}
                    compDict['sType'] = sData['sType']
                    compDict['sName'] = colsData['secondSheetNames']
                    compareData.append(compDict)
            
            # integrate different fileType list - sNameList
            for stype in sTypes:
                for compared in compareData:
                    if stype == compared['sType']:
                        pass
                


            # according to 'sType', to compare 'sName' data




    # data = []
    # firstSheetNames = []
    # for itemOne in data01:
    #     firstSheetNames.append(itemOne['sSheetName'])
    #
    # secondSheetNames = []
    # for itemTwo in data02:
    #     secondSheetNames.append(itemTwo['sSheetName'])
    #
    #
    # for first in data01:
    #     sheetInfo = {}
    #     firstSheetName = first['sSheetName']
    #     if firstSheetName not in secondSheetNames:
    #         for item in first['aCols']:
    #             item['sType'] = "player"
    #         data.append(first)
    #     else:
    #         for second in data02:
    #             if firstSheetName == second['sSheetName']:
    #                 firstsName = []
    #                 firstACols = first['aCols']
    #                 for firstACol in firstACols:
    #                     firstsName.append(firstACol['sName'])
    #
    #                 secondsName = []
    #                 secondACols = second['aCols']
    #                 for secondACol in secondACols:
    #                     secondsName.append(secondACol['sName'])
    #
    #                 aColsData = []
    #                 for firstName in firstsName:
    #                     if firstName not in secondsName:
    #                         aColsTypeDict = {}
    #                         aColsTypeDict['sName'] = firstName
    #                         aColsTypeDict['sTechName'] = ""
    #                         aColsTypeDict['sType'] = "player"
    #                         aColsData.append(aColsTypeDict)
    #                     else:
    #                         aColsDict = {}
    #                         aColsDict['sName'] = firstName
    #                         aColsDict['sTechName'] = ""
    #                         aColsData.append(aColsDict)
    #
    #
    #                 sheetInfo['sSheetName'] = firstSheetName
    #                 sheetInfo['aCols'] = aColsData
    #
    #                 data.append(sheetInfo)
    #                 break
    #
    # for second in data02:
    #     secondSheetName = second['sSheetName']
    #     if secondSheetName not in firstSheetNames:
    #         for item in second['aCols']:
    #             item['sType'] = "staff"
    #         data.append(second)
    #     else:
    #         for first in data01:
    #             if secondSheetName == first['sSheetName']:
    #                 firstsName = []
    #                 firstACols = first['aCols']
    #                 for firstACol in firstACols:
    #                     firstsName.append(firstACol['sName'])
    #
    #                 secondsName = []
    #                 secondACols = second['aCols']
    #                 for secondACol in secondACols:
    #                     secondsName.append(secondACol['sName'])
    #
    #
    #                 for secondName in secondsName:
    #                     if secondName not in firstsName:
    #                         aColsDict = {}
    #                         aColsDict['sName'] = secondName
    #                         aColsDict['sTechName'] = ""
    #                         aColsDict['sType'] = "staff"
    #                         for diffData in data:
    #                             if secondSheetName == diffData['sSheetName']:
    #                                 cols = diffData['aCols']
    #                                 cols.append(aColsDict)
    #                                 break
    #                 break

    return unioneData


def main():
    fileConts = input("请输入你想要合并的文件个数：")
    files = []
    for i in range(1, (fileConts+1)):
        fileData = {}
        fileData['fileName'] = ("Enter the path to the filename -> ")
        fileData['data'] = unicode(fileData['fileName'], "utf8")
        files.append(fileData)

    jsonDatas = []
    fileNames = []
    for fileCotent in files:
        fileName = fileCotent['fileName']
        fileNames.append(fileName)
        if os.path.isfile(fileName):
            jsonData = {}
            fileNameOpen = open(fileName, "r")
            if fileNameOpen.mode == 'r':
                contents = fileNameOpen.read()
                jsonData = json.loads(contents)
                jsonDatas.append(jsonData)
        else:
            print "Sorry, that were not a valid filename"
            continue

    file_name = ""
    for fileName in fileNames:
        file_name = file_name + os.path.splitext(fileName)[0] + "combine"

    # union json data
    uniondata = unionData(jsonDatas)

    with codecs.open(file_name+'.json', 'w', 'utf-8') as w:
        w.write(json.dumps(uniondata, ensure_ascii=False, sort_keys=True, indent=2,  separators=(',', ": ")))
    w.close()
    print "%s was created" % file_name

main()