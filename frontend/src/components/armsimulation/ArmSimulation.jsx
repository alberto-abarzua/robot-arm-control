const ArmSimulation = () => {
    const simulation_url = process.env.NEXT_PUBLIC_ARM_SIMULATION_URL;
    const websocket_port = process.env.NEXT_PUBLIC_ARM_SIMULATION_WEBSOCKET_PORT;
    const websocket_host = process.env.NEXT_PUBLIC_ARM_SIMULATION_WEBSOCKET_HOST;
    return (
        <div className="relative h-full w-full">
            <iframe
                src={`${simulation_url}/game.html?ip=${websocket_host}&port=${websocket_port}`}
                className="absolute left-0 top-0 h-full w-full cursor-none border-none"
            ></iframe>
            <div className="absolute inset-0 bg-transparent"></div>
        </div>
    );
};

export default ArmSimulation;