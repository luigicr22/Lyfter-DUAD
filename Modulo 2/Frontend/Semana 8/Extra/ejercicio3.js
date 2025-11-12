function wait(seconds) {
    return new Promise(resolve => {
        setTimeout(() => resolve(console.log(`Han pasado ${seconds} segundos`)), seconds * 1000);
    });
}

async function timer() {
    await wait(2);
    await wait(3);
    await wait(1);
}

timer();