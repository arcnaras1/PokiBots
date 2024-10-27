import gspread
gc = gspread.service_account_from_dict({
  "type": "service_account",
  "project_id": "pokibots2024innovation-project",
  "private_key_id": "7a4c8f62bff3cd0a347cf85b7e1a5839ba918c72",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCqytzVm5E08vdB\nOuG1TxAJq3JEOb+lU6JU8QJx+F44wGf/2OK0WufEZsjOHB2drGy8pvrqcMUTeqd6\n/BHqhK5YpFbOi17KXsb2REFBe0Msn9oCiMCo621Ytl0758CYA5pT2cVEwKgi7K+O\nV+QIFfvWr+xUWM/bmXqQCbUqcn3Ax/IZIJMIr2/2OgbHmxeXOyqLqGT/bV8gA97+\n+OeQkFhDmOojZtQfCLNc+C9n8wJ18/v0gbLglydwwDDlfBAflEqr7lLr1z5ridfG\nngG9vwp4DBDXJumvUb87rKWCOPAPEMjOuCC+I3LYmvsscXyZ4X3FOXP+lmUZ/W9R\nP6VbEKglAgMBAAECggEAAuLdu4BfAlGOyxvnH4y//SHYEv4U1oLkzeGqxGlJklTy\nDPlJz3lvzDpeb1k7SORWjBOYTujr86nRdbsXxGpMlfPlAaWKSwox+4xou+YM2w6y\nfPN5qgEcfnDKf44pi4gYDg2yjzhgPwLX7qRelqJkeJrNeBluHcxorVF0rcx0gpL3\nV9V+//Gr1DoKZaRVZTJqi9qbHP3Zpye5mChz817t/R02Rg7Q27v0YRczS5w2pfex\nxA9qoY00ITiLdG2tRVpLbz4IOPzJs2U7YbRU9WRLNoa7xHGDOVX6cc3t4CBaV6wi\nnTypjNoPpEgtW/qapMA4ZVBc7XCV6HjrhEmA2vfFCwKBgQDfMn4Zf0EpTXR3cwxF\n0dWrtB2bvKXsnpa/bIPaKPjdBWiXeF+y7fgQnil4fdG0M5I/ifDdvBE8zbYcuOFP\ncpnIR5sJAXCmOVHudVDkdWOC9bLeXZPfpQQjqy3bvK4E2F6pjzrEaSURo/2b+rwe\nA+cJhk0XvX92Cuw5ZY9AS/eE3wKBgQDD5LUBWh7tkvVDlgk0lMhfOjViJRWol/3h\nxCTRWJg1FBKlW5tRJNtx2K2SFvitzGpZp+Tta8GC+6VBmgYxH7rgWKjwOXO6BHdM\nYW61j0M79txsVl/qhewc1AVGz8atuLk4tEXRaCdLg3qqoQQp6roLaSoFnj2SPP2Q\ntxj1MD1PewKBgDI67dAVKHgAG27qcF+iKqEaxvMOkJTg1/I6nK3TPLaZCgHUsEzX\na1VqEtEwF6qjVI2CILf2JDb34L00CljT5LIDE2wCa/Ssv7iXpF3V4VBOtTOAAdB6\nFaVlV8u0+cDTZPJp7oLXWuVOb7vTwNRMcoldNSpbljzdlm4QYh3JOuonAoGBAJST\npAHJg8m3e9TuOD8sVal8cb7l176OwV36Md6ibpdbiSToDS6HYPXBXSx/xc+0SjmE\nEStOXnBlQxs1olqh8VB1jnTdbnv5JS7Ge3yzk1Ao1VhKTueG+eWHnhTuRIfAoqNy\nf73rXFp295PxGkJcqQ08j0XBlnuTTNL1PLXDB81/AoGBANp7rqA47zZopxqtJchI\nOGHLKbPhwYHayDWNBEPeWLjDFnbWisS8pkP5bnPU7pAopTwkkOcc7Kbw7Sz04By8\nK5054NUb98wW6w4lFx8O7+tecXsmyPyYxiJ81kViyU8T+KgjblN1BE+EsLDC2X9H\nksOw5fhzCt+lPgODMrOAx5Om\n-----END PRIVATE KEY-----\n",
  "client_email": "pokibot-bot@pokibots2024innovation-project.iam.gserviceaccount.com",
  "client_id": "114298227867609008934",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/pokibot-bot%40pokibots2024innovation-project.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
})
sh = gc.open("PokiBots Dummy Data Storage")
worksheet = sh.get_worksheet(0)
def set_value(drn, value):
    global worksheet
    worksheet.update_acell(f'A{drn + 1}', drn)
    worksheet.update_acell(f'B{drn + 1}', value)

