export default class PlantUMLServerTask {
    private serverURL;
    constructor(serverURL: string);
    generateSVG(content: string): Promise<string>;
}
