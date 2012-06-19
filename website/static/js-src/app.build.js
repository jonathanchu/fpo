({
    dir: "../gen/js",
    paths: {
        jquery: 'lib/jquery.min',
    },
    shim: {

    },
    findNestedDependencies: true,
    removeCombined: true,
    useStrict: false,
    //optimize: "none",
    modules: [
        { name: "main" }
    ]
})