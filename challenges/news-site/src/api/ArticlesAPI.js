const BASE_URL = 'http://localhost:3001/api/articles';

const tryFetch = async (url) => {
	try {
		const response = await fetch(url);
		if (!response.ok)
			throw response.statusText
		const data = await response.json();
		return data;
	} catch (err) {
		throw err;
	}
}

const fetchArticleByID = async (articleID) => {
	return await tryFetch(BASE_URL + `/${articleID}`);
};


// http://localhost:3001/api/articles?filter={"where":{"section":"opinion"}}
const fetchArticlesBySection = async (section) => {
	const data = await tryFetch(BASE_URL + `?filter={"where":{"section":"${section}"}}`);
	return data;
};

const fetchArticles = async (filters = null) => {
	const filter = filters ? `?filter=${filters}` : '';
	const data = await tryFetch(BASE_URL + filter);
	return data;
};

const searchArticles = async (term) => {
	if (term === '') {
		return await tryFetch(BASE_URL);
	} else {
		const filter = `?filter={
			"where": {
			"title": {
				"ilike": "${term}"
			}
			}
		}`;
		return await tryFetch(BASE_URL + filter);
	}
}

export default {
	fetchArticleByID,
	fetchArticles,
	fetchArticlesBySection,
	searchArticles
};
