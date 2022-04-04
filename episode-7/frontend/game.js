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

let state = {}

async function startGame() {
    state = {}

    const cmd = new InvokeCommand({FunctionName: "GameEngineInputProxy"})
    const response = await lambdaClient.send(cmd)
    const payload = asciiDecoder.decode(response.Payload)
    const gameScene = JSON.parse(payload)
    const text = gameScene.Text
    const options = JSON.parse(gameScene.Options)

    loadText(text)
    loadOptions(options)
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

function showOption(option){
    return true
}

function selectOption(option) {

}

startGame()