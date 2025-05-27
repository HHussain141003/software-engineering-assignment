import { test, expect } from '@playwright/test';

// Date and Time in the format DD/MM/YYYY, HH:MM:SS (e.g. 15/05/2024, 06:58:39)
function current_date() {
  var date1 = new Date();
  var formattedDate = new Intl.DateTimeFormat("en-GB", {
  year: "numeric",
  month: "2-digit",
  day: "2-digit",
  hour: "2-digit",
  minute: "2-digit",
  second: "2-digit",
  hour12: false,
  }).format(date1);

  return formattedDate
}

let recordID = `Playwright automated test run at ${current_date()}`

test.beforeEach(async ({ page }, testInfo) => {
  console.log(`Running test: ${testInfo.title}`);
  await page.goto('http://127.0.0.1:5000/');
  await page.getByRole('textbox', { name: 'Username:' }).click();
  await page.getByRole('textbox', { name: 'Username:' }).fill('admin');
  await page.getByRole('textbox', { name: 'Password:' }).click();
  await page.getByRole('textbox', { name: 'Password:' }).fill('admin123');
  await page.getByRole('button', { name: 'Login' }).click();
  });
  
test.afterEach("Status check", async ({ page }, testInfo) => {
console.log(`Finished ${testInfo.title} with status ${testInfo.status}`);
});

test('01 - View all tickets', async ({ page }) => {
  await page.goto('http://127.0.0.1:5000/home');
  await page.getByRole('button', { name: 'View all tickets' }).click();
  await expect(page.locator('div').nth(2)).toBeVisible();
});

test('02 - Create new ticket', async ({ page }) => {
  await page.goto('http://127.0.0.1:5000/home');
  await page.getByRole('button', { name: 'New ticket' }).click();
  await page.getByRole('textbox', { name: 'Title:' }).click();
  await page.getByRole('textbox', { name: 'Title:' }).fill(recordID);
  await page.getByRole('textbox', { name: 'Description:' }).click();
  await page.getByRole('textbox', { name: 'Description:' }).fill(recordID);
  await page.getByRole('button', { name: 'Submit' }).click();
});

test('03 - Edit ticket', async ({ page }) => {
  await page.goto('http://127.0.0.1:5000/view_tickets/1?prev_page=http://127.0.0.1:5000/admin_view_all_tickets');
  await page.getByRole('link', { name: 'Edit Ticket' }).click();
  await page.getByLabel('Status:').selectOption('On Hold');
  await page.getByRole('textbox', { name: 'Description:' }).click();
  await page.getByRole('textbox', { name: 'Description:' }).press('ControlOrMeta+a');
  await page.getByRole('textbox', { name: 'Description:' }).fill(recordID);
  await page.getByRole('button', { name: 'Save Changes' }).click();
});

test('04 - Add comment', async ({ page }) => {
  await page.goto('http://127.0.0.1:5000/home');
  await page.getByRole('button', { name: 'View all tickets' }).click();
  await page.getByRole('row', { name: '2 Broken Printer The office' }).getByRole('link').click();
  await page.getByRole('textbox', { name: 'Write your comment here...' }).click();
  await page.getByRole('textbox', { name: 'Write your comment here...' }).fill(recordID);
  await page.getByRole('button', { name: 'Post Comment' }).click();
});

test('05 - Add a new user', async ({ page }) => {
  await page.goto('http://127.0.0.1:5000/home');
  await page.getByRole('button', { name: 'Add a new user' }).click();
  await page.getByRole('textbox', { name: 'Username:' }).click();
  await page.getByRole('textbox', { name: 'Username:' }).fill('playwrightuser');
  await page.getByRole('textbox', { name: 'Email:' }).click();
  await page.getByRole('textbox', { name: 'Email:' }).fill('playwrightuser@no-reply.com');
  await page.getByRole('textbox', { name: 'Password:' }).click();
  await page.getByRole('textbox', { name: 'Password:' }).fill('enter123');
  await page.getByRole('button', { name: 'Add User' }).click();
});

test('06 - Logout', async ({ page }) => {
  await page.goto('http://127.0.0.1:5000/home');
  page.once('dialog', dialog => {
    console.log(`Dialog message: ${dialog.message()}`);
    dialog.accept().catch(() => {});
  });
  await page.getByRole('button', { name: 'Logout' }).click();
});