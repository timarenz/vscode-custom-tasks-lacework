# vscode-custom-tasks-lacework

This repostiry contains an example on how to include the Lacework vulnerability scanner into Visual Studio Code.

## Preqrequists

In order to use this example make sure you have installed and configured the following components:

- Visual Studio Code [https://code.visualstudio.com]
- Docker for Desktop [https://www.docker.com/products/docker-desktop]
- Docker extension for Visual Studio Code [https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker]
- lacework-vulnerability-scanner v0.2.0 or later installed in a system path [https://github.com/lacework/lacework-vulnerability-scanner]
- Configure inline scanner authentication or set enviromnet variables as per our documentation [https://support.lacework.com/hc/en-us/articles/1500001777821-Integrate-Inline-Scanner#configuration-commands]

## Demonstration

- Clone this repository and open it in Visual Studio Code
- Open the command palette (Command + Shift + P) on Mac and enter "Run Task"
- Now you have several options, either run the different "Lacework: ..." commands by its own or run everything at once using the "Lacework: Build, scan and delete Docker image for vulnerabilities" task
- Result of the vulnerability scan will be output in the integrated terminall

[Demo video](https://raw.githubusercontent.com/timarenz/vscode-custom-tasks-lacework/main/images/demoscan.gif)
