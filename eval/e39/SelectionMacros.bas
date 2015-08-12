Attribute VB_Name = "Module1"
Sub AppendCells()
Attribute AppendCells.VB_ProcData.VB_Invoke_Func = " \n14"

Dim delimiter As String
Dim row As Integer
Dim rowText As String
Dim nextRowText As String

Dim startTextCol As Integer
Dim col As Integer
Dim allColText As String
Dim nextColText As String

row = 1
nextRowText = "something"
delimiter = vbTab
startTextCol = 3


Do While (Len(nextRowText) > 0)

    rowText = Cells(row, 1).Value
    
    allColText = ""
    nextColText = "default"
    col = startTextCol
    Do While (Len(nextColText) > 0)
        If (Len(allColText) > 0) Then
            allColText = allColText + delimiter + Cells(row, col).Value
        Else
            allColText = Cells(row, col).Value
        End If
        Cells(row, col).ClearContents
        nextColText = Cells(row, col + 1)
        col = col + 1
    Loop
    
    Cells(row, startTextCol).Value = allColText
    nextRowText = Cells(row + 1, 1)
    row = row + 1
    
Loop

End Sub
Sub ToCSV()

Dim delimiter As String
Dim row As Integer
Dim rowText As String
Dim nextRowText As String

Dim col As Integer
Dim colText As String
Dim allColText As String
Dim nextColText As String

Dim FileStr As String
FileStr = Application.GetSaveAsFilename()
If FileStr = "False" Then
    Exit Sub
End If
Debug.Print (FileStr)

Open FileStr For Output As #1

row = 1
nextRowText = "something"
delimiter = ",,,"

Do While (Len(nextRowText) > 0)

    rowText = Cells(row, 1).Value
    
    allColText = ""
    nextColText = "default"
    col = 1
    Do While (Len(nextColText) > 0)
        colText = CStr(Cells(row, col).Value)
        If (Len(allColText) > 0) Then
            allColText = allColText + delimiter + colText
        Else
            allColText = colText
        End If
        nextColText = CStr(Cells(row, col + 1))
        col = col + 1
    Loop
    
    Print #1, allColText
    nextRowText = Cells(row + 1, 1)
    row = row + 1
    
Loop

Close #1

End Sub
