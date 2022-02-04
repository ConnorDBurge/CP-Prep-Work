import ArticlesAPI from './ArticlesAPI';
import fetchMock from 'fetch-mock'
require('isomorphic-fetch')

afterEach(() => {
  fetchMock.restore()
})


it('calls ArticlesAPI.fetchArticleByID(1)', async () => {
  fetchMock.get('http://localhost:3001/api/articles/1', { success: true })
  const res = await ArticlesAPI.fetchArticleByID(1)
  expect(await res.success).toBe(true)
})

it('calls ArticlesAPI.fetchArticles()', async () => {
  fetchMock.get('http://localhost:3001/api/articles', { success: true })
  const res = await ArticlesAPI.fetchArticles()
  expect(await res.success).toBe(true)
})

it('calls ArticlesAPI.fetchArticlesBySection(\'opinion\')', async () => {
  fetchMock.get('http://localhost:3001/api/articles?filter={"where":{"section":"opinion"}}', { success: true })
  const res = await ArticlesAPI.fetchArticlesBySection('opinion')
  expect(await res.success).toBe(true)
})


it('submits an article by calling addArticle()', (done) => {
  const request = fetchMock.post('http://localhost:3001/api/articles', { success: true });
  const articleObject = { title: 'test', byline: 'title', abstract: 'adsf' };
  return ArticlesAPI.addArticle(articleObject)
    .then((json) => {
      const requestBody = request._calls[0][1].body;
      expect(JSON.parse(requestBody)).toEqual(articleObject);
      expect(json.ok).toEqual(true);
      done();
    })
    .catch((err) => {
      throw new Error('Call failed');
    });
});
