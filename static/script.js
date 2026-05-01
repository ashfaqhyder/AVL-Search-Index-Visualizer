const keywordInput = document.getElementById("keywordInput");
const messageBox = document.getElementById("message");
const avlTreeArea = document.getElementById("avlTree");
const bstTreeArea = document.getElementById("bstTree");
const rotationType = document.getElementById("rotationType");
const avlHeight = document.getElementById("avlHeight");
const bstHeight = document.getElementById("bstHeight");
const heightDifference = document.getElementById("heightDifference");
const searchSteps = document.getElementById("searchSteps");

const sampleKeywords = [
    "algorithm",
    "backend",
    "cache",
    "database",
    "engine",
    "flask",
    "google",
    "hashing",
    "index",
    "javascript",
    "keyword",
    "latency",
    "metadata",
    "network",
    "python",
    "query",
    "ranking",
    "search",
    "tree",
    "url",
];

async function apiPost(route, keyword = "") {
    const response = await fetch(route, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ keyword }),
    });

    if (!response.ok) {
        throw new Error("Request failed");
    }

    return response.json();
}

async function apiGet(route) {
    const response = await fetch(route);

    if (!response.ok) {
        throw new Error("Request failed");
    }

    return response.json();
}

async function handleAction(route, button = null) {
    const keyword = keywordInput.value.trim();

    try {
        setLoading(button, true);
        const data = await apiPost(route, keyword);
        updateUi(data.tree, data.message, data.status);
    } catch (error) {
        messageBox.textContent = "Unable to connect to the Flask server.";
        messageBox.className = "message error";
    } finally {
        setLoading(button, false);
    }
}

function updateUi(data, message = "Tree data loaded.", status = "success") {
    const metrics = data.metrics;
    const searchedKeyword = metrics.last_search.keyword;

    messageBox.textContent = message;
    messageBox.className = `message ${status}`;

    rotationType.textContent = metrics.rotation;
    avlHeight.textContent = metrics.avl_height;
    bstHeight.textContent = metrics.bst_height;
    heightDifference.textContent = metrics.height_difference;
    searchSteps.textContent = `AVL ${metrics.last_search.avl_steps} | BST ${metrics.last_search.bst_steps}`;

    renderTree(avlTreeArea, data.avl, searchedKeyword);
    renderTree(bstTreeArea, data.bst, searchedKeyword);
}

function renderTree(container, treeData, searchedKeyword) {
    container.innerHTML = "";

    if (!treeData) {
        const empty = document.createElement("div");
        empty.className = "empty-tree";
        empty.textContent = "No keywords indexed yet.";
        container.appendChild(empty);
        return;
    }

    const tree = document.createElement("div");
    tree.className = "tree";
    tree.appendChild(buildNode(treeData, searchedKeyword));
    container.appendChild(tree);
}

function buildNode(node, searchedKeyword) {
    const li = document.createElement("li");

    const nodeBox = document.createElement("div");
    nodeBox.className = node.keyword === searchedKeyword ? "node found" : "node";

    const key = document.createElement("span");
    key.className = "node-key";
    key.title = node.keyword;
    key.textContent = node.keyword;

    const meta = document.createElement("span");
    meta.className = "node-meta";
    meta.textContent = node.balance === null
        ? `h:${node.height}`
        : `h:${node.height} | bf:${node.balance}`;

    nodeBox.appendChild(key);
    nodeBox.appendChild(meta);
    li.appendChild(nodeBox);

    if (node.left || node.right) {
        const children = document.createElement("ul");

        if (node.left) {
            children.appendChild(buildNode(node.left, searchedKeyword));
        } else {
            children.appendChild(buildEmptyChild());
        }

        if (node.right) {
            children.appendChild(buildNode(node.right, searchedKeyword));
        } else {
            children.appendChild(buildEmptyChild());
        }

        li.appendChild(children);
    }

    return li;
}

function buildEmptyChild() {
    const li = document.createElement("li");
    const placeholder = document.createElement("div");
    placeholder.className = "node";
    placeholder.style.opacity = "0";
    placeholder.textContent = ".";
    li.appendChild(placeholder);
    return li;
}

function randomKeyword() {
    const keyword = sampleKeywords[Math.floor(Math.random() * sampleKeywords.length)];
    keywordInput.value = keyword;
    keywordInput.focus();
}

function setLoading(button, isLoading) {
    if (!button) {
        return;
    }

    button.classList.toggle("is-loading", isLoading);
    button.disabled = isLoading;
}

document.getElementById("insertBtn").addEventListener("click", (event) => handleAction("/insert", event.currentTarget));
document.getElementById("deleteBtn").addEventListener("click", (event) => handleAction("/delete", event.currentTarget));
document.getElementById("searchBtn").addEventListener("click", (event) => handleAction("/search", event.currentTarget));
document.getElementById("randomBtn").addEventListener("click", randomKeyword);
document.getElementById("resetBtn").addEventListener("click", async (event) => {
    try {
        setLoading(event.currentTarget, true);
        const data = await apiPost("/reset");
        keywordInput.value = "";
        updateUi(data.tree, data.message, data.status);
    } catch (error) {
        messageBox.textContent = "Unable to reset because the Flask server is not responding.";
        messageBox.className = "message error";
    } finally {
        setLoading(event.currentTarget, false);
    }
});

keywordInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        handleAction("/insert", document.getElementById("insertBtn"));
    }
});

apiGet("/get_tree_data")
    .then((data) => updateUi(data, "Ready to index keywords."))
    .catch(() => {
        messageBox.textContent = "Start the Flask server to load tree data.";
        messageBox.className = "message warning";
    });
