pytest -s -v -m "sanity" --html=./Reports/reportChrome.html testCases/ --browser chrome
pytest -s -v -m "sanity" --html=./Reports/reportFirefox.html testCases/ --browser firefox

rem chrome
rem pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser chrome
rem pytest -s -v -m "sanity and regression" --html=./Reports/report.html testCases/ --browser chrome
rem pytest -s -v -m "regression" --html=./Reports/report.html testCases/ --browser chrome

rem firefox
rem pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser firefox
rem pytest -s -v -m "sanity and regression" --html=./Reports/report.html testCases/ --browser firefox
rem pytest -s -v -m "regression" --html=./Reports/report.html testCases/ --browser firefox