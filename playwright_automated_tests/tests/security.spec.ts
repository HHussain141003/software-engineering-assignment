import { test, expect } from '@playwright/test';

test.beforeEach(async ({ page }, testInfo) => {
    console.log(`Running Test: ${testInfo.title}`);
  });
  
test.afterEach("Status check", async ({ page }, testInfo) => {
console.log(`Finished Test: ${testInfo.title} with status ${testInfo.status}`);
});

// User 1 tries to access a record with ID 2 which belongs to another user, User 1 should be redirected to the view tickets screen.
test('A01:2021 - Broken Access Control', async ({ page }) => {
  await page.goto('http://127.0.0.1:5000/');
  await page.getByRole('textbox', { name: 'Username:' }).click();
  await page.getByRole('textbox', { name: 'Username:' }).fill('user1');
  await page.getByRole('textbox', { name: 'Password:' }).click();
  await page.getByRole('textbox', { name: 'Password:' }).fill('user1');
  await page.getByRole('button', { name: 'Login' }).click();
  await page.goto('http://127.0.0.1:5000/view_tickets/2');
  await expect(page).toHaveURL("http://127.0.0.1:5000/view_tickets");
});

// This test tries to exploit the Username input by entering an SQL Statement, however it does not work as all the queries in the application are parameterised.
test('A03:2021 - Injection', async ({ page }) => {
  await page.goto('http://127.0.0.1:5000/');
  await page.getByRole('textbox', { name: 'Username:' }).click();
  await page.getByRole('textbox', { name: 'Username:' }).fill("admin' OR '1'='1");
  await page.getByRole('textbox', { name: 'Password:' }).click();
  await page.getByRole('textbox', { name: 'Password:' }).fill("wrongpassword");
  await page.getByRole('button', { name: 'Login' }).click();
  await expect(page).toHaveURL("http://127.0.0.1:5000/");
  await expect(page.locator('#flash-messages')).toContainText('Invalid username or password, please try again.');
});
