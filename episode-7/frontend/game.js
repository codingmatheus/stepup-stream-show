import {fromCognitoIdentityPool} from "@aws-sdk/credential-providers"
import {LambdaClient, InvokeCommand} from "@aws-sdk/client-lambda"

const REGION = "eu-west-1"

const lambdaClient = new LambdaClient(
    {
        region: REGION,
        credentials: fromCognitoIdentityPool({
            clientConfig: {region: REGION },
            identityPoolId: "eu-west-1:b82a3df4-970a-4aff-ac90-e34502269625"
        })
    
})

const textElement = document.getElementById("text")
const optionButtonsElement = document.getElementById("option-buttons")
const asciiDecoder = new TextDecoder("ascii")

let username = ""
let taskToken = ""
let gameId = ""

document.addEventListener("DOMContentLoaded", (event) => {
    document.getElementById("gameCanvas").style.display = "none"
    document.getElementById("startButton").addEventListener("click", loadGame, false)
})

function loadGame() {

    const loginElement = document.getElementById("loginPanel")
    const gameElement = document.getElementById("gameCanvas")
    const usernameElement = document.getElementById("username")

    username = usernameElement.value
    loginElement.style.display = "none"
    gameElement.style.display = "block"

    loadNextScreen("")
}

async function loadNextScreen(choiceId)
{
    const gameScene = await getNextGameScene(choiceId)
    const text = gameScene.Text
    const options = JSON.parse(gameScene.Options)
    taskToken = gameScene.TaskToken
    gameId = gameScene.GameId
    
    loadText(text)
    loadOptions(options)
}

async function getNextGameScene(choiceId)
{
    const gameSceneRequest = {username: username, gameId: gameId, taskToken: taskToken, choice: choiceId}
    const input = JSON.stringify(gameSceneRequest)
    const cmd = new InvokeCommand({FunctionName: "GameEngineProxy", Payload: input})
    const response = await lambdaClient.send(cmd)
    const payload = asciiDecoder.decode(response.Payload)
    const gameScene = JSON.parse(payload)

    return gameScene
}

function clearOptions()
{
     while(optionButtonsElement.firstChild) {
        optionButtonsElement.removeChild(optionButtonsElement.firstChild)
    }
}

function loadText(text) {

    textElement.innerText = text
}

function loadOptions(options) {
    clearOptions()

    options.forEach(option => {
        const button = document.createElement("button")
        button.innerText = option.text
        button.classList.add("btn")
        button.addEventListener("click", () => selectOption(option))

        optionButtonsElement.appendChild(button)
    })
}

function selectOption(choice) {
    loadNextScreen(choice)
}