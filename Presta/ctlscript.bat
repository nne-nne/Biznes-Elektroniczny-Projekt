@echo off
rem START or STOP Services
rem ----------------------------------
rem Check if argument is STOP or START

if not ""%1"" == ""START"" goto stop

if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\hypersonic\scripts\ctl.bat (start /MIN /B C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\server\hsql-sample-database\scripts\ctl.bat START)
if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\ingres\scripts\ctl.bat (start /MIN /B C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\ingres\scripts\ctl.bat START)
if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\mysql\scripts\ctl.bat (start /MIN /B C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\mysql\scripts\ctl.bat START)
if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\postgresql\scripts\ctl.bat (start /MIN /B C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\postgresql\scripts\ctl.bat START)
if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\apache\scripts\ctl.bat (start /MIN /B C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\apache\scripts\ctl.bat START)
if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\openoffice\scripts\ctl.bat (start /MIN /B C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\openoffice\scripts\ctl.bat START)
if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\apache-tomcat\scripts\ctl.bat (start /MIN /B C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\apache-tomcat\scripts\ctl.bat START)
if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\resin\scripts\ctl.bat (start /MIN /B C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\resin\scripts\ctl.bat START)
if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\jetty\scripts\ctl.bat (start /MIN /B C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\jetty\scripts\ctl.bat START)
if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\subversion\scripts\ctl.bat (start /MIN /B C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\subversion\scripts\ctl.bat START)
rem RUBY_APPLICATION_START
if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\lucene\scripts\ctl.bat (start /MIN /B C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\lucene\scripts\ctl.bat START)
if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\third_application\scripts\ctl.bat (start /MIN /B C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\third_application\scripts\ctl.bat START)
goto end

:stop
echo "Stopping services ..."
if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\third_application\scripts\ctl.bat (start /MIN /B C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\third_application\scripts\ctl.bat STOP)
if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\lucene\scripts\ctl.bat (start /MIN /B C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\lucene\scripts\ctl.bat STOP)
rem RUBY_APPLICATION_STOP
if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\subversion\scripts\ctl.bat (start /MIN /B C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\subversion\scripts\ctl.bat STOP)
if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\jetty\scripts\ctl.bat (start /MIN /B C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\jetty\scripts\ctl.bat STOP)
if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\hypersonic\scripts\ctl.bat (start /MIN /B C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\server\hsql-sample-database\scripts\ctl.bat STOP)
if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\resin\scripts\ctl.bat (start /MIN /B C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\resin\scripts\ctl.bat STOP)
if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\apache-tomcat\scripts\ctl.bat (start /MIN /B /WAIT C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\apache-tomcat\scripts\ctl.bat STOP)
if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\openoffice\scripts\ctl.bat (start /MIN /B C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\openoffice\scripts\ctl.bat STOP)
if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\apache\scripts\ctl.bat (start /MIN /B C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\apache\scripts\ctl.bat STOP)
if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\ingres\scripts\ctl.bat (start /MIN /B C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\ingres\scripts\ctl.bat STOP)
if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\mysql\scripts\ctl.bat (start /MIN /B C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\mysql\scripts\ctl.bat STOP)
if exist C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\postgresql\scripts\ctl.bat (start /MIN /B C:\Users\adaml\Documents\Biznes-Elektroniczny-Projekt\Presta\postgresql\scripts\ctl.bat STOP)

:end

