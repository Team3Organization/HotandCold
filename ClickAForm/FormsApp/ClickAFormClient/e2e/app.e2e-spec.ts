import { FormsGeneratorPage } from './app.po';

describe('forms-generator App', function() {
  let page: FormsGeneratorPage;

  beforeEach(() => {
    page = new FormsGeneratorPage();
  });

  it('should display message saying app works', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('app works!');
  });
});
