cd C:\
mkdir LAB6
cd LAB6
wmic os get Caption > os.txt
wmic os get FreePhysicalMemory,TotalVisibleMemorySize > memory.txt
wmic logicaldisk get name,description > discs.txt

mkdir TEST
copy /Y C:\LAB6\* C:\LAB6\TEST\*
cd TEST

copy /Y C:\LAB6\*.txt C:\LAB6\TEST\all.txt

for %i in (*.*) do if NOT %i == all.txt del %i
