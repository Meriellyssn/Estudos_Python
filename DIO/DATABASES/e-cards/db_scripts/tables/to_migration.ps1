# Pegar o diretorio atual
$scriptDirectory = Split-Path -Path $MyInvocation.MyCommand.Definition -Parent

# Arquivo de Saída com todos os sql (Corrigido: adicionado $ em $scriptDirectory)
$outputFile = Join-Path -Path $scriptDirectory -ChildPath "migration.sql"

# Verificar se o arquivo já existe, se existir delete.
if (Test-Path $outputFile) {
    Remove-Item $outputFile
}

# Pegar Conteúdo dos arquivos
$sqlFiles = Get-ChildItem -Path $scriptDirectory -Filter *.sql -File | Sort-Object Name

# Concatenar Arquivos (Corrigido: "GO" agora é inserido em uma linha separada)
foreach($file in $sqlFiles) {
    Get-Content $file.FullName | Out-File -Append -FilePath $outputFile
    "GO" | Out-File -Append -FilePath $outputFile
}

Write-Host "Todos Arquivos foram combinados em $outputFile"
