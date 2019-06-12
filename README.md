# python-unionconfigurablefiles

union multiple json files, and point out different from other files and set 'sType' property:
1. configurabel different files
2. union and add 'sType' property
3. json format:
[
  {
    "aCols": [
      {
        "sName": "First Name名字",
        "sTechName": ""
      },
      {
        "sName": "Last Name姓氏",
        "sTechName": ""
      },
      {
        "sName": "Jersey Name球衣名字",
        "sTechName": "",
        "sType": "player"
      },
      {
        "sName": "Identity Card身份证号",
        "sTechName": ""
      },
      {
        "sName": "Date of Birth出生日期",
        "sTechName": ""
      },
      {
        "sName": "Gender性别",
        "sTechName": ""
      },
      {
        "sName": "Place of Birth出生地",
        "sTechName": ""
      },
      {
        "sName": "Country of Birth出生国家/地区",
        "sTechName": ""
      },
      {
        "sName": "Nationality国籍",
        "sTechName": ""
      },
      {
        "sName": "2nd Nationality第二国籍",
        "sTechName": ""
      },
      {
        "sName": "Height身高（cm）",
        "sTechName": "",
        "sType": "player"
      },
      {
        "sName": "Weight体重（kg）",
        "sTechName": "",
        "sType": "player"
      },
      {
        "sName": "Foot惯用脚",
        "sTechName": "",
        "sType": "player"
      },
      {
        "sName": "Standing Leg站立腿",
        "sTechName": "",
        "sType": "player"
      },
      {
        "sName": "Shoe Size球鞋尺寸",
        "sTechName": ""
      },
      {
        "sName": "Jersey Size球衣尺寸",
        "sTechName": ""
      },
      {
        "sName": "Shorts Size短裤尺寸",
        "sTechName": ""
      },
      {
        "sName": "Highest Degree最高学历",
        "sTechName": "",
        "sType": "player"
      },
      {
        "sName": "Education教育背景",
        "sTechName": "",
        "sType": "player"
      },
      {
        "sName": "Educational Goal教育目标",
        "sTechName": "",
        "sType": "player"
      },
      {
        "sName": "Alias别名",
        "sTechName": ""
      },
      {
        "sName": "Player License球员许可",
        "sTechName": "",
        "sType": "player"
      }
    ],
    "sSheetName": "General Info基本信息"
  },
  {
    "aCols": [
      {
        "sName": "First Name名字",
        "sTechName": ""
      },
      {
        "sName": "Identity Card身份证号",
        "sTechName": ""
      },
      {
        "sName": "Team球队",
        "sTechName": ""
      },
      {
        "sName": "Area领域",
        "sTechName": ""
      },
      {
        "sName": "Role角色",
        "sTechName": ""
      },
      {
        "sName": "Jersey No.球衣号码",
        "sTechName": "",
        "sType": "player"
      },
      {
        "sName": "Member From生效日期",
        "sTechName": ""
      },
      {
        "sName": "Member To到期日期",
        "sTechName": ""
      },
      {
        "sName": "Type(Team/ Club)类型",
        "sTechName": "",
        "sType": "staff"
      }
    ],
    "sSheetName": "Assignments分配"
  },
  {
    "aCols": [
      {
        "sName": "First Name名字",
        "sTechName": ""
      },
      {
        "sName": "Identity Card身份证号",
        "sTechName": ""
      },
      {
        "sName": "Communication Channel渠道",
        "sTechName": ""
      },
      {
        "sName": "Main Social Media是否主要",
        "sTechName": ""
      },
      {
        "sName": "Social Media Type类型（私人、工作等）",
        "sTechName": ""
      },
      {
        "sName": "Social Media Name内容（电子邮件、电话号码、社交媒体号等）",
        "sTechName": ""
      }
    ],
    "sSheetName": "Communication社交信息"
  },
  {
    "aCols": [
      {
        "sName": "First Name名字",
        "sTechName": ""
      },
      {
        "sName": "Identity Card身份证号",
        "sTechName": ""
      },
      {
        "sName": "Address Type地址类型",
        "sTechName": ""
      },
      {
        "sName": "Street街道",
        "sTechName": ""
      },
      {
        "sName": "House No.门牌号",
        "sTechName": ""
      },
      {
        "sName": "ZIP Code邮政编码",
        "sTechName": ""
      },
      {
        "sName": "City城市",
        "sTechName": ""
      },
      {
        "sName": "Country国家/地区",
        "sTechName": ""
      },
      {
        "sName": "Main Address主要地址",
        "sTechName": ""
      }
    ],
    "sSheetName": "Addresses地址"
  },
  {
    "aCols": [
      {
        "sName": "First Name名字",
        "sTechName": ""
      },
      {
        "sName": "Identity Card身份证号",
        "sTechName": ""
      },
      {
        "sName": "Nationality国籍",
        "sTechName": ""
      },
      {
        "sName": "Number编号",
        "sTechName": ""
      },
      {
        "sName": "From从",
        "sTechName": ""
      },
      {
        "sName": "To到",
        "sTechName": ""
      },
      {
        "sName": "Issuing Authority签发机构",
        "sTechName": ""
      },
      {
        "sName": "Comment备注",
        "sTechName": ""
      },
      {
        "sName": "Country签证国家/地区",
        "sTechName": ""
      },
      {
        "sName": "Visa ID签证ID",
        "sTechName": ""
      },
      {
        "sName": "Type of Visa签证类型",
        "sTechName": ""
      },
      {
        "sName": "Date of Issue签发日期",
        "sTechName": ""
      },
      {
        "sName": "Date of Expiry到期日",
        "sTechName": ""
      }
    ],
    "sSheetName": "Passport护照"
  },
  {
    "aCols": [
      {
        "sName": "Foot惯用脚",
        "sTechName": ""
      },
      {
        "sName": "Standing Leg站立腿",
        "sTechName": ""
      },
      {
        "sName": "Jersey Size球衣尺寸",
        "sTechName": ""
      },
      {
        "sName": "Shorts Size短裤尺寸",
        "sTechName": ""
      },
      {
        "sName": "Gender性别",
        "sTechName": ""
      },
      {
        "sName": "Country/ Nationality 国家/国籍",
        "sTechName": ""
      },
      {
        "sName": "Area领域",
        "sTechName": ""
      },
      {
        "sName": "Role角色",
        "sTechName": ""
      },
      {
        "sName": "Team球队",
        "sTechName": ""
      },
      {
        "sName": "Communication Channel渠道",
        "sTechName": ""
      },
      {
        "sName": "Type(Team/ Club)类型",
        "sTechName": "",
        "sType": "staff"
      }
    ],
    "sSheetName": "Code List Reference数据参照"
  }
]
