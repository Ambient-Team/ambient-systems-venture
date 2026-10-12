This file is a merged representation of the entire codebase, combined into a single document by Repomix.

<file_summary>
This section contains a summary of this file.

<purpose>
This file contains a packed representation of the entire repository's contents.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.
</purpose>

<file_format>
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  - File path as an attribute
  - Full contents of the file
</file_format>

<usage_guidelines>
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.
</usage_guidelines>

<notes>
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)
</notes>

</file_summary>

<directory_structure>
.firebase/hosting.YnVpbGQ.cache
.firebaserc
.gitignore
AWSCLIV2.pkg
cors.json
firebase.json
package.json
public/404.html
public/index.html
public/Logo.png
public/manifest.json
README.md
src/Dashboard.js
src/DataLibraryPage.js
src/DataPageComponents/AddDataPage.js
src/DataPageComponents/FinishImport.js
src/DataPageComponents/ImportDataComponents/DataMapping.js
src/DataPageComponents/ImportDataComponents/SelectDataSource.js
src/DataPageComponents/ImportDataComponents/UploadData.js
src/DataPageComponents/ImportDataPage.js
src/DataPageComponents/ManualInputComponents/ManualDataEntryTable.js
src/DataPageComponents/ManualInputPage.js
src/DataPageComponents/SyncDataPage.js
src/EditProfileBox.js
src/FinancePage.js
src/FinancePageComponents/ActionPlanPage.js
src/FinancePageComponents/DataSelectionPage.js
src/FinancePageComponents/EditMetricBox.js
src/FinancePageComponents/GoalMetricsComponents/GoalMetricsDetailBox.js
src/FinancePageComponents/GoalMetricsPage.js
src/FinancePageComponents/PlanningComponents/PlanningDetailBox.js
src/FinancePageComponents/PlanningPage.js
src/firebase-config.js
src/index.js
src/OnboardPage.js
src/OverviewPage.js
src/OverviewPageComponents/dataStatusTable.js
src/OverviewPageComponents/FinancialMetricsTable.js
src/OverviewPageComponents/operationalMetricsTable.js
src/OverviewPageComponents/recommendationTable.js
src/pics/AmbientLogo_Colour-01.svg
src/pics/aws_logo.png
src/pics/aws_logo.svg
src/pics/AzureLogo.png
src/pics/GeotabLogo.jpg
src/pics/Logo_White-01.svg
src/pics/Logo_White-03.svg
src/pics/No_Image_Available.jpeg
src/pics/SamsaraLogo.jpg
src/ProfilePage.js
src/ProfileSettingPage.js
src/ServiceRequestPage.js
src/ServiceRequestPageComponents/AddData.js
src/ServiceRequestPageComponents/CreateNewRequestPage.js
src/ServiceRequestPageComponents/MyRequestsPage.js
src/SignInPage.js
src/SignUpPage.js
src/SummaryPage.js
</directory_structure>

<files>
This section contains the contents of the repository's files.

<file path=".firebase/hosting.YnVpbGQ.cache">
404.html,1724954544359,05cbc6f94d7a69ce2e29646eab13be2c884e61ba93e3094df[redacted]d18b3
asset-manifest.json,1724954556705,20b7e53c7c3c52f8e2566924e79f79bb94eda98c06f0edc3edf81e7cdab52ca1
index.html,1724954556705,d1b763f488f69c9cebcada0667fe0f8e8dcf7164c5264deb25abb5f7202c5720
manifest.json,1724954544365,38b7a6434abfbadc23521bee6ce930354b1742529da0b0af32fb201220da7169
Logo.png,1724954544360,0798102923c55b74ac3e4a128337d2758f6b8e563ea827812eebad3617ef8c5e
static/js/main.20c57891.js.LICENSE.txt,1724954556735,573f08a930703db03a33e0ec03631f5532ebc457b846cf0e95887bb9469fc896
static/media/Logo_White-01.a51bd5c85b7d123114102023db871d26.svg,1724954556734,87b4aadb01d7e3f99851afa1b3be458c22d0e70b407e06896ee574686ab38e66
static/media/Logo_White-03.13f6869fe1d769dace7599f199c803e8.svg,1724954556734,978a05c8f4d961f78cd84a953efc725f131a6c229166d4fa78443fdb1a2d3b69
static/media/AmbientLogo_Colour-01.0ace086884c9a843f0b34d69da19adbc.svg,1724954556735,aca025a5aef7156ac325c8ff46b0309806aedfb1617a38195d62dbc11d2cf177
static/media/aws_logo.850296a094250f4a242e.png,1724954556735,00f841ef90b27b959e3f91f9a23931ae6c4ba619ac94fdab63c19372ad99bb1b
static/js/main.20c57891.js,1724954556734,4efb1402d85e03b95e4eaa203999a7adfb8f1d66b1a6b1fe7884459d5afec45a
static/js/main.20c57891.js.map,1724954556737,702e37d9162dd6e583536f47f0e6ebba76d0f012bbc9577546f67208b1273065
</file>

<file path=".firebaserc">
{
  "projects": {
    "default": "[redacted-project]"
  }
}
</file>

<file path=".gitignore">
node_modules

# production
build
</file>

<file path="cors.json">
{
    "CORSRules": [
      {
        "AllowedOrigins": ["*"],
        "AllowedMethods": ["GET", "POST", "PUT", "DELETE", "HEAD"],
        "AllowedHeaders": ["*"],
        "MaxAgeSeconds": 3000,
        "ExposeHeaders": ["ETag", "x-amz-meta-custom-header"]
      }
    ]
  }
</file>

<file path="firebase.json">
{
  "hosting": {
    "public": "build",
    "ignore": [
      "firebase.json",
      "**/.*",
      "**/node_modules/**"
    ],
    "rewrites": [
      {
        "source": "**",
        "destination": "/index.html"
      }
    ]
  },
  "emulators": {
    "hosting": {
      "port": 5033
    },
    "ui": {
      "enabled": true
    }
  }
}
</file>

<file path="package.json">
{
  "name": "my-app",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
    "@emotion/react": "^11.9.0",
    "@emotion/styled": "^11.8.1",
    "@google-cloud/aiplatform": "^1.19.0",
    "@google-cloud/bigquery": "^6.0.1",
    "@mui/icons-material": "^5.8.0",
    "@mui/material": "^5.8.0",
    "@mui/styled-engine-sc": "^5.8.0",
    "@mui/x-date-pickers": "^7.11.1",
    "@testing-library/jest-dom": "^5.16.4",
    "@testing-library/react": "^13.2.0",
    "@testing-library/user-event": "^13.5.0",
    "axios": "^0.27.2",
    "buffer": "^6.0.3",
    "dayjs": "^1.11.12",
    "emailjs-com": "^3.2.0",
    "firebase": "^9.23.0",
    "fs": "^0.0.1-security",
    "mui-calendar-picker": "^1.0.10",
    "primeicons": "^5.0.0",
    "primereact": "^8.1.0",
    "react": "^18.1.0",
    "react-dom": "^18.1.0",
    "react-dropzone": "^14.2.2",
    "react-router-dom": "^6.3.0",
    "react-scripts": "^5.0.1",
    "react-scrollbars-custom": "^4.1.1",
    "react-transition-group": "^4.4.2",
    "recharts": "^2.1.9",
    "styled-components": "^5.3.5",
    "web-vitals": "^2.1.4"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "devDependencies": {
    "firebase-tools": "^8.20.0"
  }
}
</file>

<file path="public/404.html">
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Page Not Found</title>

    <style media="screen">
      body { background: #ECEFF1; color: rgba(0,0,0,0.87); font-family: Roboto, Helvetica, Arial, sans-serif; margin: 0; padding: 0; }
      #message { background: white; max-width: 360px; margin: 100px auto 16px; padding: 32px 24px 16px; border-radius: 3px; }
      #message h3 { color: #888; font-weight: normal; font-size: 16px; margin: 16px 0 12px; }
      #message h2 { color: #ffa100; font-weight: bold; font-size: 16px; margin: 0 0 8px; }
      #message h1 { font-size: 22px; font-weight: 300; color: rgba(0,0,0,0.6); margin: 0 0 16px;}
      #message p { line-height: 140%; margin: 16px 0 24px; font-size: 14px; }
      #message a { display: block; text-align: center; background: #039be5; text-transform: uppercase; text-decoration: none; color: white; padding: 16px; border-radius: 4px; }
      #message, #message a { box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24); }
      #load { color: rgba(0,0,0,0.4); text-align: center; font-size: 13px; }
      @media (max-width: 600px) {
        body, #message { margin-top: 0; background: white; box-shadow: none; }
        body { border-top: 16px solid #ffa100; }
      }
    </style>
  </head>
  <body>
    <div id="message">
      <h2>404</h2>
      <h1>Page Not Found</h1>
      <p>The specified file was not found on this website. Please check the URL for mistakes and try again.</p>
      <h3>Why am I seeing this?</h3>
      <p>This page was generated by the Firebase Command-Line Interface. To modify it, edit the <code>404.html</code> file in your project's configured <code>public</code> directory.</p>
    </div>
  </body>
</html>
</file>

<file path="public/index.html">
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/Logo.png" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content="Web site created using create-react-app"
    />
    <link rel="apple-touch-icon" href="%PUBLIC_URL%/logo192.png" />
    <!--
      manifest.json provides metadata used when your web app is installed on a
      user's mobile device or desktop. See https://developers.google.com/web/fundamentals/web-app-manifest/
    -->
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
    <!--
      Notice the use of %PUBLIC_URL% in the tags above.
      It will be replaced with the URL of the `public` folder during the build.
      Only files inside the `public` folder can be referenced from the HTML.

      Unlike "/favicon.ico" or "favicon.ico", "%PUBLIC_URL%/favicon.ico" will
      work correctly both with client-side routing and a non-root public URL.
      Learn how to configure a non-root public URL by running `npm run build`.
    -->

    <!-- This provides loading functionality when redirecting pages. -->
    <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>

    <title>Ambient Systems</title>
  </head>
  <body>
    <div id="root">
      <div class="preload-title">
        Hold on, it's loading!
      </div>
    </div>
    <!--
      This HTML file is a template.
      If you open it directly in the browser, you will see an empty page.

      You can add webfonts, meta tags, or analytics to this file.
      The build step will place the bundled scripts into the <body> tag.

      To begin the development, run `npm start` or `yarn start`.
      To create a production bundle, use `npm run build` or `yarn build`.
    -->
  </body>
</html>
</file>

<file path="public/manifest.json">
{
  "short_name": "Ambient App",
  "name": "Ambientsystems Application",
  "icons": [
    {
      "src": "Logo.png",
      "sizes": "64x64 32x32 24x24 16x16",
      "type": "image/png"
    },
    {
      "src": "logo192.png",
      "type": "image/png",
      "sizes": "192x192"
    },
    {
      "src": "logo512.png",
      "type": "image/png",
      "sizes": "512x512"
    }
  ],
  "start_url": ".",
  "display": "standalone",
  "theme_color": "#000000",
  "background_color": "#ffffff"
}
</file>

<file path="README.md">
# ambient-platform-demo
</file>

<file path="src/Dashboard.js">
import * as React from 'react';
import { styled, alpha, createTheme, ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import MuiDrawer from '@mui/material/Drawer';
import Switch, { SwitchProps } from '@mui/material/Switch';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import List from '@mui/material/List';
import Divider from '@mui/material/Divider';
import InputBase from '@mui/material/InputBase';
import ListItemButton from '@mui/material/ListItemButton';
import DashboardIcon from '@mui/icons-material/Dashboard';
import PersonIcon from '@mui/icons-material/Person';
import SettingsIcon from '@mui/icons-material/Settings';
import BarChartIcon from '@mui/icons-material/BarChart';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import ListItemText from '@mui/material/ListItemText';
import ListItemIcon from '@mui/material/ListItemIcon';
import NotificationsIcon from '@mui/icons-material/Notifications';
import AddIcon from '@mui/icons-material/Add';
import TableRowsIcon from '@mui/icons-material/TableRows';
import CheckIcon from '@mui/icons-material/Check';
import CloseIcon from '@mui/icons-material/Close';
import ButtonBase from '@mui/material/ButtonBase';
import Logo from './pics/Logo_White-01.svg';
import colorLogo from './pics/AmbientLogo_Colour-01.svg';
import {
  useNavigate,
   Outlet
} from "react-router-dom";
import { useState, useEffect } from 'react';
import { getDownloadURL, getStorage, ref } from 'firebase/storage';
import { getFirestore, getDoc, doc, collection, onSnapshot, query, where, limit, orderBy } from 'firebase/firestore'
import { getAuth, signOut } from "firebase/auth";
import firebaseApp from './firebase-config';

// Connect to current firebase project
const storage = getStorage(firebaseApp);
const firestore = getFirestore(firebaseApp);

const Search = styled('div')(({ theme }) => ({
  position: 'relative',
  borderRadius: theme.shape.borderRadius,
  backgroundColor: theme.palette.error.main,
  '&:hover': {
    backgroundColor: alpha(theme.palette.common.white, 0.25),
  },
  marginRight: theme.spacing(2),
  marginLeft: 0,
  width: '100%',
  [theme.breakpoints.up('sm')]: {
    marginLeft: theme.spacing(110),
    width: 'auto',
  },
}));

const SearchIconWrapper = styled('div')(({ theme }) => ({
  padding: theme.spacing(0, 2),
  height: '100%',
  position: 'absolute',
  pointerEvents: 'none',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
}));

const StyledInputBase = styled(InputBase)(({ theme }) => ({
  color: 'inherit',
  '& .MuiInputBase-input': {
    padding: theme.spacing(1, 1, 1, 0),
    // vertical padding + font size from searchIcon
    paddingLeft: `calc(1em + ${theme.spacing(4)})`,
    transition: theme.transitions.create('width'),
    width: '100%',
    [theme.breakpoints.up('md')]: {
      width: '20ch',
    },
  },
}));

const drawerWidth = 210;

// const AppBar = styled(MuiAppBar, {
//   shouldForwardProp: (prop) => prop !== 'open',
// })(({ theme, open }) => ({
//   zIndex: theme.zIndex.drawer + 1,
//   transition: theme.transitions.create(['width', 'margin'], {
//     easing: theme.transitions.easing.sharp,
//     duration: theme.transitions.duration.leavingScreen,
//   }),
//   ...(open && {
//     marginLeft: drawerWidth,
//     width: `calc(100% - ${drawerWidth}px)`,
//     transition: theme.transitions.create(['width', 'margin'], {
//       easing: theme.transitions.easing.sharp,
//       duration: theme.transitions.duration.enteringScreen,
//     }),
//   }),
// }));

const Drawer = styled(MuiDrawer, { shouldForwardProp: (prop) => prop !== 'open' })(
  ({ theme, open }) => ({
    '& .MuiDrawer-paper': {
      position: 'relative',
      whiteSpace: 'nowrap',
      width: drawerWidth,
      transition: theme.transitions.create('width', {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.enteringScreen,
      }),
      boxSizing: 'border-box',
      backgroundColor: theme.palette.background.drawer,
      ...(!open && {
        overflowX: 'hidden',
        transition: theme.transitions.create('width', {
          easing: theme.transitions.easing.sharp,
          duration: theme.transitions.duration.leavingScreen,
        }),
        width: theme.spacing(7),
        [theme.breakpoints.up('sm')]: {
          width: theme.spacing(9),
        },
      }),
    },
  }),
);

const mdTheme = createTheme({
  palette: {
    mode: 'dark',
    background: {
      default: '#031c4a',
      paper: '#031c4a',
      drawer: '#031c4a'
    },
    error: {
      main: '#060c43',
    },
    warning: {
      main: '#00e676',
    },
    success: {
      main: '#ffb74d',
    },
  },
});

const ndTheme = createTheme({
  palette: {
    mode: 'light',
    background: {
      default: '#ffffff',
      paper: '#ffffff',
      drawer: '#E0EDFB'
    },
  },
});

const MaterialUISwitch = styled(Switch)(({ theme }) => ({
  width: 62,
  height: 34,
  padding: 7,
  '& .MuiSwitch-switchBase': {
    margin: 1,
    padding: 0,
    transform: 'translateX(6px)',
    '&.Mui-checked': {
      color: '#fff',
      transform: 'translateX(22px)',
      '& .MuiSwitch-thumb:before': {
        backgroundImage: `url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" height="20" width="20" viewBox="0 0 20 20"><path fill="${encodeURIComponent(
          '#fff',
        )}" d="M4.2 2.5l-.7 1.8-1.8.7 1.8.7.7 1.8.6-1.8L6.7 5l-1.9-.7-.6-1.8zm15 8.3a6.7 6.7 0 11-6.6-6.6 5.8 5.8 0 006.6 6.6z"/></svg>')`,
      },
      '& + .MuiSwitch-track': {
        opacity: 1,
        backgroundColor: theme.palette.mode === 'dark' ? '#8796A5' : '#aab4be',
      },
    },
  },
  '& .MuiSwitch-thumb': {
    backgroundColor: theme.palette.mode === 'dark' ? '#003892' : '#001e3c',
    width: 32,
    height: 32,
    '&:before': {
      content: "''",
      position: 'absolute',
      width: '100%',
      height: '100%',
      left: 0,
      top: 0,
      backgroundRepeat: 'no-repeat',
      backgroundPosition: 'center',
      backgroundImage: `url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" height="20" width="20" viewBox="0 0 20 20"><path fill="${encodeURIComponent(
        '#fff',
      )}" d="M9.305 1.667V3.75h1.389V1.667h-1.39zm-4.707 1.95l-.982.982L5.09 6.072l.982-.982-1.473-1.473zm10.802 0L13.927 5.09l.982.982 1.473-1.473-.982-.982zM10 5.139a4.872 4.872 0 00-4.862 4.86A4.872 4.872 0 0010 14.862 4.872 4.872 0 0014.86 10 4.872 4.872 0 0010 5.139zm0 1.389A3.462 3.462 0 0113.471 10a3.462 3.462 0 01-3.473 3.472A3.462 3.462 0 016.527 10 3.462 3.462 0 0110 6.528zM1.665 9.305v1.39h2.083v-1.39H1.666zm14.583 0v1.39h2.084v-1.39h-2.084zM5.09 13.928L3.616 15.4l.982.982 1.473-1.473-.982-.982zm9.82 0l-.982.982 1.473 1.473.982-.982-1.473-1.473zM9.305 16.25v2.083h1.389V16.25h-1.39z"/></svg>')`,
    },
  },
  '& .MuiSwitch-track': {
    opacity: 1,
    backgroundColor: theme.palette.mode === 'dark' ? '#8796A5' : '#aab4be',
    borderRadius: 20 / 2,
  },
}));

// Main function of this page
function DashboardContent() {
  const [fff, setFFF] = React.useState("dark");
  const [open, setOpen] = React.useState(true);

  const [anchorEl, setAnchorEl] = React.useState(null);
  const [anchorEl2, setAnchorEl2] = React.useState(null);
  const [anchorEl3, setAnchorEl3] = React.useState(null);

  const isMenuOpen = Boolean(anchorEl);
  const isMenuOpen2 = Boolean(anchorEl2);
  const isMenuOpen3 = Boolean(anchorEl3);

  const handleProfileMenuOpen = (event) => {
    setAnchorEl(event.currentTarget);
  };
  const handleInfoMenuOpen = (event) => {
    setAnchorEl2(event.currentTarget);
  };
  const handleMessageMenuOpen = (event) => {
    setAnchorEl3(event.currentTarget);
    setNum(0)
  };

  const handleMenuClose = () => {
    setAnchorEl(null);
  };
  const handleMenuClose2 = () => {
    setAnchorEl2(null);
  };
  const handleMenuClose3 = () => {
    setAnchorEl3(null);
  };
  const handleSignOut = () => {
    const auth = getAuth();
    auth.signOut()
    window.localStorage.removeItem('access_token');
    window.location.reload();
  }
  
  /* Droplists of head bar buttons */
  /* Droplist of Message/First button */
  const [alerts, setAlerts] = useState([]);
  const [num, setNum] = useState(0);

  function formatDate() {
    var d = new Date(),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2) 
        month = '0' + month;
    if (day.length < 2) 
        day = '0' + day;

    return [year, month, day].join('-');
  }

  useEffect(() => {
    const alertQuery = query(
      collection(firestore, 'alerts'),
      where('email', '==', user_email),
      where('date', '==', formatDate()),
      orderBy("time", "desc"),
      limit(5)
    );
      const unsubscribe = onSnapshot(alertQuery, snapshot => {
        setAlerts(snapshot.docs.map(doc => ({id: doc.id, data: doc.data() })))
        setNum(1)
      })

      return () => {
        unsubscribe()
      }
  }, [])

  const renderMessageMenu = (
    <Menu
      anchorEl={anchorEl3}
      anchorOrigin={{
        vertical: 'top',
        horizontal: 'right',
      }}
      keepMounted
      transformOrigin={{
        vertical: 'top',
        horizontal: 'right',
      }}
      open={isMenuOpen3}
      onClose={handleMenuClose3}
    >
    {alerts?.map((row) => (
      <MenuItem onClick={handleMenuClose3}>
        <ListItemIcon>
          <NotificationsIcon fontSize="small"/>
        </ListItemIcon>
        <ListItemText>
          {row.data.content}
        </ListItemText>
      </MenuItem>
    ))}
    </Menu>
  );

  /* Droplist of Information/Second button */
  const renderInfoMenu = (
    <Menu
      anchorEl={anchorEl2}
      anchorOrigin={{
        vertical: 'top',
        horizontal: 'right',
      }}
      keepMounted
      transformOrigin={{
        vertical: 'top',
        horizontal: 'right',
      }}
      open={isMenuOpen2}
      onClose={handleMenuClose2}
    >
      <MenuItem onClick={handleMenuClose2}>
        <ListItemIcon>
          <CheckIcon fontSize="small"/>
        </ListItemIcon>
        <ListItemText>
          Your project is running well. 
        </ListItemText>
      </MenuItem>
      <MenuItem onClick={handleMenuClose2}>
        <ListItemIcon>
          <CheckIcon fontSize="small" />
        </ListItemIcon>
        <ListItemText>
          All services are ready. 
        </ListItemText>
      </MenuItem>
      <MenuItem onClick={handleMenuClose2}>
        <ListItemIcon>
          <CloseIcon fontSize="small" />
        </ListItemIcon>
        <ListItemText>
          Some information missed. 
        </ListItemText>
      </MenuItem>
    </Menu>
  );
  
  /* Droplist of Profile/Third button */
  const renderMenu = (
    <Menu
      anchorEl={anchorEl}
      anchorOrigin={{
        vertical: 'top',
        horizontal: 'right',
      }}
      keepMounted
      transformOrigin={{
        vertical: 'top',
        horizontal: 'right',
      }}
      open={isMenuOpen}
      onClose={handleMenuClose}
    >
      <MenuItem onClick={handleSignOut}>Sign out</MenuItem>
    </Menu>
  );

  /* Identify the current user */
  const user_email = window.localStorage.getItem('user_email');

  /* Set-up avatar */
  const [avatar, setAvatar] = useState([])

  const [payWall, setPayWall] = useState(false)
  useEffect(() => {
    const authQuery = query(
      collection(firestore, 'users'),
      where('username', '==', user_email),
    );
    onSnapshot(authQuery, snapshot => {
        const t = (snapshot.docs.map(doc => ({ data: doc.data().isUpgrade })))
        if (!t[0].data) {
            setPayWall(true)
        }
    })
  }, [])

  useEffect(() => {
    if (!user_email) {
      setAvatar('https://cdn.icon-icons.com/icons2/1378/PNG/512/avatardefault_92824.png')
    } else {
      const avatarRef = ref(storage, user_email+'/avatar.png')
      getDownloadURL(avatarRef)
      .then((url) => {
        setAvatar(url)
      })
      .catch((error) => {
        switch (error.code) {
          case 'storage/object-not-found':
            setAvatar('https://cdn.icon-icons.com/icons2/1378/PNG/512/avatardefault_92824.png')
            break;

          case 'storage/unknown':
            console.log("Unknown error!")
            break;
        }})
    }
  }, [])

  const [myTheme, setMyTheme] = useState(ndTheme)

  return (
    <ThemeProvider theme={myTheme}>
      <Box sx={{ display: 'flex' }}>
        <CssBaseline />

        {/* Head bar layout */}
        {/* <AppBar position="absolute" open={open}>
          <Toolbar
            sx={{
              pr: '24px', // keep right padding when drawer closed
              backgroundColor: (theme) =>
              theme.palette.mode === 'light'
                ? theme.palette.grey[200]
                : theme.palette.background.default,
            }}
          > */}

            {/* Placeholder */}
            {/* <Box sx={{ flexGrow: 1 }} />

            <FormControlLabel
              control={<MaterialUISwitch  onChange={() => myTheme === ndTheme? setMyTheme(mdTheme)  : setMyTheme(ndTheme)} />}
            />

          </Toolbar>
        </AppBar> */}
        {/* {renderInfoMenu} */}
        {renderMessageMenu}
        {renderMenu}

            {/* Side bar layout */}
            <Drawer variant="permanent" open={open}>
              {/* Logo at the top left cornor */}
              <Toolbar
                sx={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'flex-end',
                  px: [1],
                  height: 130,
                }}
              >
                <ButtonBase href='/Dashboard/Welcome' fullWidth>
                  {myTheme === mdTheme? (<img src={Logo} alt="Logo" width={180} height={75}/>) : (<img src={colorLogo} alt="Logo" width={180} height={75}/>)}
                </ButtonBase>
              </Toolbar>
              <Divider />

              {/* Navigations to different pages */}
              <List component="nav" sx={{ flexGrow: 1 }}>
                {/* Overview */}
                <[Third party]"/Dashboard/Overview" >
                    <ListItemIcon>
                      <DashboardIcon />
                    </ListItemIcon>
                    <ListItemText primary="Overview" />
                </ListItemButton>


                {/* Finance */}
                <[Third party]"/Dashboard/Finance/Planning" >
                    <ListItemIcon>
                      <TableRowsIcon />
                    </ListItemIcon>
                    <ListItemText primary="Finance" />
                </ListItemButton>

                {/* Data Library */}
                <[Third party]"/Dashboard/Data/DataLibrary" >
                    <ListItemIcon>
                      <BarChartIcon />
                    </ListItemIcon>
                    <ListItemText primary="Data" />
                </ListItemButton>

                {/* Service Requests */}
                <[Third party]"/Dashboard/ServiceRequest" >
                    <ListItemIcon>
                      <AddIcon />
                    </ListItemIcon>
                    <ListItemText primary="Service Requests" />
                </ListItemButton>
                </List>

                <List component="nav">
                {/* Profile */}
                <[Third party]"/Dashboard/Profile" >
                    <ListItemIcon>
                      <PersonIcon />
                    </ListItemIcon>
                    <ListItemText primary="Profile" />
                </ListItemButton>


                {/* Notification */}
                <[Third party]"" >
                    <ListItemIcon>
                      <NotificationsIcon />
                    </ListItemIcon>
                    <ListItemText primary="Notification" />
                </ListItemButton>

                {/* Settings */}
                <[Third party]"/Dashboard/Profile/Settings" >
                    <ListItemIcon>
                      <SettingsIcon />
                    </ListItemIcon>
                    <ListItemText primary="Settings" />
                </ListItemButton>

              </List>
            </Drawer>

        {/* Main space of page, which is blank in this page */}
        <Box
          component="main"
          sx={{
            backgroundColor: (theme) =>
              theme.palette.mode === 'light'
                ? theme.palette.grey[100]
                : theme.palette.error.main,
            flexGrow: 1,
            height: '100vh',
            overflow: 'auto',
          }}
        >
          <Toolbar /> 
          <Outlet />
        </Box>
      </Box>
    </ThemeProvider>
  );
}

export default function Dashboard() {
  /* Identify the current user */
  const user_email = window.localStorage.getItem('user_email');
  
  const navigate = useNavigate()

  const userCheck = async () => {
    const snapShot = await getDoc(doc(firestore, 'users/'+user_email))
    if (!snapShot.exists()) {
      navigate("/Onboard")
    }
    else {
      const userQuery = query(
        collection(firestore, 'users'),
        where('username', '==', user_email),
        limit(1)
        );

      onSnapshot(userQuery, snapshot => {
          const currentUser = snapshot.docs.map(doc => ({id: doc.id, data: doc.data() }))
          window.localStorage.setItem('industry', currentUser[0].data.industry)
      })
    }
  };

  useEffect(() => {
  const auth = getAuth();
  const token =  window.localStorage.getItem('access_token');
  if(!token || !user_email) navigate("/");
  else userCheck();
  },[])
    
  return <DashboardContent />;
}
</file>

<file path="src/DataLibraryPage.js">
import * as React from 'react';
import { useState, useEffect } from "react";
import { Table, TableContainer, TableHead, TableRow, TableCell, 
    TableBody, Paper, Button, Box, ListItem, Typography, 
    Select, MenuItem, Pagination, TextField } from '@mui/material';
import firebaseApp from './firebase-config';
import { getFirestore, collection, onSnapshot, query, where, } from 'firebase/firestore'
import ErrorIcon from '@mui/icons-material/Error';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';

// Connect to current firebase project
const firestore = getFirestore(firebaseApp);

export default function DataLibraryPage() {
    const user_email = window.localStorage.getItem('user_email');
    const [userDataList, setUserDataList] = useState([]);
    const [selectedMetrics, setSelectedMetrics] = useState([]);
    const [metrics, setMetrics] = useState([]);
    const industry = window.localStorage.getItem('industry');

    const [currentPage, setCurrentPage] = useState(1);
    const [itemsPerPage, setItemsPerPage] = useState(10);

    // Calculate the total number of pages
    const totalPages = Math.ceil(userDataList.length / itemsPerPage);

    // Slice the user data list based on current page and items per page
    const paginatedData = userDataList.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage);

    const handleChangePage = (event, newPage) => {
        setCurrentPage(newPage);
    };

    const handleItemsPerPageChange = (event) => {
        setItemsPerPage(event.target.value);
        setCurrentPage(1); // Reset to first page on items per page change
    };

    useEffect(() => {
        const userDataQuery = query(
            collection(firestore, 'userData'),
            where('user_email', '==', user_email),
            where('selected', '==', true),
        );
    
        const unsubscribe = onSnapshot(userDataQuery, snapshot => {
              let userData = snapshot.docs.map(doc => doc.data());
              userData.forEach(data => {
                const linkedMetrics = selectedMetrics.filter(metric => data.metricIds.includes(metric.metricID));
                data.linkedMetrics = linkedMetrics
                const linkedMetricText = linkedMetrics.map(metric => metric.metricName).join(', ');
    
                // Combine the linkedMetrics into string
                data.linkedMetricText = linkedMetricText;
            });
            
              setUserDataList(userData);
            })
    
            return () => {
            unsubscribe()
            }
        }, [selectedMetrics]);

    const handleNavigation = (url) => {
        window.location.href = url;
    };

    useEffect(() => {
        const userQuery = query(
            collection(firestore, 'users'),
            where('email', '==', user_email),
        );
    
        const unsubscribe = onSnapshot(userQuery, snapshot => {
                let users = snapshot.docs.map(doc => doc.data());
                const selectedMetricIds = users[0].selectedMetricIds
                const selectedMetricList = metrics
                    .filter(metric => selectedMetricIds.includes(metric.id))
                    .map(metric => ({
                        metricID: metric.id,
                        metricName: metric.name,
                        metricType: metric.type,
                        metricTech: metric.tech,
                    }));
                setSelectedMetrics(selectedMetricList);
            })
    
            return () => {
            unsubscribe()
            }
        }, [metrics]);

    useEffect(() => {
        const metricQuery = query(
            collection(firestore, 'metrics'),
            where('industry', '==', industry),
        );
    
        const unsubscribe = onSnapshot(metricQuery, snapshot => {
                let metrics = snapshot.docs.map(doc => doc.data());
                
                setMetrics(metrics);
            })
    
            return () => {
            unsubscribe()
            }
        }, []);


    const handleAddData = () =>{
        if (userDataList.length > 0){
            handleNavigation('DataLibrary/AddData')
        }
        else{
            alert("No data options available. Please select metrics in Finance/GOAL METRICS page.")
        }
    }
    return (
            
        <Box sx={{ flexGrow: 1, maxWidth: 1504, height: '100vh'}}>

        <ListItem>
            <Typography
                component="h1"
                variant="h6"
                color="inherit"
                noWrap
                sx={{ flexGrow: 1, fontWeight: 'bold', mt:2, ml:2, mb:2, mr: 3 }}
            >
                Data Library
            </Typography>
        </ListItem>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', ml:4, mb: 2 }}>
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
                {/* <TextField
                    variant="outlined"
                    placeholder="Search..."
                    size="small"
                    sx={{ minWidth: 200 }}
                /> */}
                {/* <Select
                    defaultValue=""
                    variant="outlined"
                    size="small"
                    displayEmpty
                    sx={{ minWidth: 120 }}
                >
                    <MenuItem value="">Metric</MenuItem>
                    <MenuItem value="metric1">Metric 1</MenuItem>
                    <MenuItem value="metric2">Metric 2</MenuItem>
                </Select> */}
                {/* <Select
                    defaultValue=""
                    variant="outlined"
                    size="small"
                    displayEmpty
                    sx={{ minWidth: 120 }}
                >
                    <MenuItem value="">Type</MenuItem>
                    <MenuItem value="type1">Type 1</MenuItem>
                    <MenuItem value="type2">Type 2</MenuItem>
                </Select> */}
                {/* <Select
                    defaultValue=""
                    variant="outlined"
                    size="small"
                    displayEmpty
                    sx={{ minWidth: 120 }}
                >
                    <MenuItem value="">Date</MenuItem>
                    <MenuItem value="date1">Date 1</MenuItem>
                    <MenuItem value="date2">Date 2</MenuItem>
                </Select> */}
            </Box>
            <Button variant="contained" color="primary" onClick={() => handleAddData()}>
                ADD DATA
            </Button>
        </Box>
        <TableContainer component={Paper} sx={{ ml: 4, mr: 4, display: 'flex' }}>
            <Table>
                <TableHead>
                    <TableRow>
                        {/* <TableCell sx={{ fontWeight: 'bold' }}>Icon/Photo</TableCell> */}
                        <TableCell sx={{ fontWeight: 'bold' }}>Data Option Name</TableCell>
                        <TableCell sx={{ fontWeight: 'bold' }}>Description</TableCell>
                        <TableCell sx={{ fontWeight: 'bold' }}>Linked Metric(s)</TableCell>
                        {/* <TableCell sx={{ fontWeight: 'bold' }}>Data Source Type</TableCell> */}
                        <TableCell sx={{ fontWeight: 'bold' }}>Status</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {paginatedData.map((item, index) => (
                        item.status === "On Track" ? (
                            <TableRow key={index}>
                                {/* <TableCell>Add</TableCell> */}
                                <TableCell>{item.name}</TableCell>
                                <TableCell>{item.description}</TableCell>
                                <TableCell>{item.linkedMetricText}</TableCell>
                                <TableCell><CheckCircleIcon sx={{ color: 'blue' }} /></TableCell>
                            </TableRow>
                        ) : (
                            <TableRow key={index}>
                                {/* <TableCell>Add</TableCell> */}
                                <TableCell>{item.name}</TableCell>
                                <TableCell>{item.description}</TableCell>
                                <TableCell>{item.linkedMetricText}</TableCell>
                                <TableCell><ErrorIcon sx={{ color: 'red' }} /></TableCell>
                            </TableRow>
                        )
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
        <Box sx={{ display: 'flex', justifyContent: 'flex-end', alignItems: 'center', mt: 2, ml: 4, mr: 4 }}>
            <Select
                value={itemsPerPage}
                onChange={handleItemsPerPageChange}
            >
                <MenuItem value={5}>5</MenuItem>
                <MenuItem value={10}>10</MenuItem>
                <MenuItem value={15}>15</MenuItem>
            </Select>
            <Pagination
                count={totalPages}
                page={currentPage}
                onChange={handleChangePage}
            />
        </Box>
    </Box>
    );
}
</file>

<file path="src/DataPageComponents/AddDataPage.js">
import * as React from 'react';
import { useState, useEffect } from "react";
import { Grid, Paper, Box, Typography, Button, Stack } from '@mui/material';
import { Link } from 'react-router-dom';

export default function AddDataPage() {

    return (
            
        <Box sx={{ padding: 4 }}>
           <Box>
            <Typography variant="h6" sx={{ mb: 8, fontWeight: 'bold' }}>
                <Link to="/Dashboard/Data/DataLibrary" style={{ textDecoration: 'underline', color: 'inherit' }}>
                    Data Library
                </Link>
                {' / '}
                <span style={{ color: 'gray' }}>Add Data</span>
            </Typography>
        </Box>
            <Typography variant="h6" sx={{ textAlign: 'center', mb: 6 }}>
                Select your data source
            </Typography>
            <Grid container spacing={4} justifyContent="center">
                <Grid item>
                <Link to="/Dashboard/Data/DataLibrary/AddData/ManualInput" style={{ color: 'inherit', fontWeight: 'bold' }}>
                    <Paper
                        sx={{
                            height: 150,
                            width: 200,
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'center',
                            cursor: 'pointer',
                            boxShadow: 3,
                        }}
                        elevation={3}
                    >
                        <Stack
                        direction="column"
                        spacing={0.5}
                        alignItems="center"
                        justifyContent="center"
                        sx={{ width: '100%' }}
                        >
                        <Typography
                        
                        >Manual Input</Typography>
                        </Stack>
                    </Paper> 
                    </Link>
                </Grid>
                <Grid item>
                <Link to="/Dashboard/Data/DataLibrary/AddData/ImportData" style={{ color: 'inherit', fontWeight: 'bold' }}>
                    <Paper
                        sx={{
                            height: 150,
                            width: 200,
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'center',
                            cursor: 'pointer',
                            boxShadow: 3,
                        }}
                        elevation={3}
                    >
                        <Stack
                        direction="column"
                        spacing={0.5}
                        alignItems="center"
                        justifyContent="center"
                        sx={{ width: '100%' }}
                        >
                        <Typography sx={{ whiteSpace: 'nowrap' }}
                        >
                            Import
                        </Typography>
                        </Stack>
                    </Paper>
                    </Link>
                </Grid>
                <Grid item>
                <Link to="/Dashboard/Data/DataLibrary/AddData/SyncData" style={{ color: 'inherit', fontWeight: 'bold' }}>
                    <Paper
                        sx={{
                        height: 150,
                        width: 200,
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        cursor: 'pointer',
                        boxShadow: 3,
                        }}
                        elevation={3}
                    >
                        <Stack
                        direction="column"
                        spacing={0.5}
                        alignItems="center"
                        justifyContent="center"
                        sx={{ width: '100%' }}
                        >
                        <Typography sx={{ whiteSpace: 'nowrap' }}>Sync (Real-Time)</Typography>
                        </Stack>
                    </Paper>
                    </Link>
                </Grid>
            </Grid>
        </Box>
    );
}
</file>

<file path="src/DataPageComponents/FinishImport.js">
import React from 'react';
import [Third party], Button, Paper } from '@mui/material';
import CheckCircleOutlineIcon from '@mui/icons-material/CheckCircleOutline';
import { Link } from 'react-router-dom';

export default function FinishImport({datasource}) {
  return (
    <Paper 
        sx={{ padding: 4, display: 'flex', flexDirection: 'column', height: '80%', justifyContent: 'center',
        alignItems: 'center', textAlign: 'center',
     }}>
      <CheckCircleOutlineIcon sx={{ fontSize: 60, color: 'green', mb: 2 }} />
      {datasource == "Sync" ? (
      <Typography variant="h5" sx={{ mb: 8}}>
        Successfully selected the Sync API
      </Typography>
      ) : (
      <Typography variant="h5" sx={{ mb: 8}}>
        Data successfully imported!
      </Typography>
      )
    }
      <Box sx={{ display: 'flex', gap: 2,}}>
        <Button component={Link} to="/Dashboard/Data/DataLibrary" sx={{ color: 'blue', fontWeight: 'bold' }}>
          BACK TO DATA LIBRARY
        </Button>
        <Button component={Link} to="/Dashboard/Data/DataLibrary/AddData" sx={{ color: 'blue', fontWeight: 'bold' }}>
          ADD NEW DATA
        </Button>
      </Box>
    </Paper>
  );
}
</file>

<file path="src/DataPageComponents/ImportDataComponents/DataMapping.js">
import React, { useState } from 'react';
import {
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  TextField,
  MenuItem,
  Typography,
  Box,
  Button
} from '@mui/material';
import emailjs from "emailjs-com";
import firebaseApp from '../../firebase-config';
import { getFirestore, doc, collection, getDocs, updateDoc, limit, query, where, addDoc } from 'firebase/firestore'
import { getStorage, ref, uploadBytes, } from "firebase/storage";

const firestore = getFirestore(firebaseApp);
const storage = getStorage(firebaseApp);
const user_email = window.localStorage.getItem('user_email');

export default function DataMapping({ 
    setCurrentStep, 
    selectedDataOption, 
    tmpheader, 
    mapping, 
    setMapping, 
    selectedFormat,
    selectedDate,
    filename,
    file,
}) {

  const handleMappingChange = (field, value) => {
    setMapping({
      ...mapping,
      [field]: value,
    });
  };

  const checkAllFieldsMapped = () => {
    if (selectedDataOption.fields.length > 0){
    const allMapped = selectedDataOption.fields.every(
      (field) => mapping[field]
    );
    return allMapped;
  }
  else{
    const allMapped = selectedDataOption.dummyFields.every(
      (field) => mapping[field]
    );
    return allMapped;
  }
  };

  const handleFileUpload = () => {
    const userRef = ref(storage, user_email+'/'+filename)
    uploadBytes(userRef, file).then((snapshot) => {
        console.log("Uploaded file!")
        alert("Upload successfully!")
    
        emailjs.send("teamService","template_cqyfsfh",{
            subject: "User uploaded a new file!",
            name: "File name is " + filename,
            email: "from " + user_email,
            message: "Please check in the firebase storage",
        }, "r87tnpnYE2FXwhAzx");

        const email = user_email
        const content = "Uploaded a file : " + filename
        const date = formatDate()
        const time = new Date()
        addDoc(collection(firestore, 'alerts'), {email, content, date, time})
        handleUpdateUserDataRecord();

    }).catch((error) => {
        console.error("Error getting documents: ", error);
        alert("Failed to upload data. Please try again.");
    });
  };

  const handleUpdateUserDataRecord = () => {
    let importData = selectedDataOption.importData
    let newImportData = [
        ...importData,
        {
            date : selectedDate.format('ddd MMM DD YYYY'),
            filename : filename,
            format : selectedFormat,
            mapping : mapping,
        }
    ]
    
    importData = newImportData

    console.log(importData)

    const q = query(collection(firestore, 'userData'), where("id", "==", selectedDataOption.id));

    getDocs(q).then((querySnapshot) => {
        querySnapshot.forEach((queryDocSnapshot) => {
            // Get the document reference
            const docRef = doc(firestore, 'userData', queryDocSnapshot.id);
    
            // Update the document with the new data
            updateDoc(docRef, { importData, status: "On Track" })
                .then(() => {
                    console.log("Metric value updated successfully!");
                    setCurrentStep(3)
                })
                .catch((error) => {
                    console.error("Error updating document: ", error);
                    alert("Failed to upload data. Please try again.");
                });
        });
    }).catch((error) => {
        console.error("Error getting documents: ", error);
        alert("Failed to upload data. Please try again.");
    });

  }

  function formatDate() {
    var d = new Date(),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();
  
    if (month.length < 2) 
        month = '0' + month;
    if (day.length < 2) 
        day = '0' + day;
  
    return [year, month, day].join('-');
  }

  const handleNext = () => {
    if (!checkAllFieldsMapped()) {
        alert("Please map all the fields");
        return
    } 
    handleFileUpload()
  };



  return (
    <Paper sx={{ padding: 4 }}>
      <Typography variant="h6" sx={{ textAlign: 'center', mb: 4 }}>
        [Third party]
      </Typography>
      <TableContainer>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell><strong>Fields</strong></TableCell>
              <TableCell><strong>Map to Header</strong></TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {selectedDataOption.fields.length > 0 ? (
            selectedDataOption.fields.map((field, index) => (
              <TableRow key={index}>
                <TableCell sx={{ width: '50%' }}>{field}</TableCell>
                <TableCell>
                  <TextField
                    select
                    value={mapping[field] || ''}
                    onChange={(event) =>
                      handleMappingChange(field, event.target.value)
                    }
                    
                    sx={{ width: '50%' }}
                  >
                    {tmpheader.map((headerOption, idx) => (
                      <MenuItem key={idx} value={headerOption}>
                        {headerOption}
                      </MenuItem>
                    ))}
                  </TextField>
                </TableCell>
              </TableRow>
            ))) : 
            (
              selectedDataOption.dummyFields.map((dummyField, index) => (
                <TableRow key={index}>
                  <TableCell sx={{ width: '50%' }}>{dummyField}</TableCell>
                  <TableCell>
                    <TextField
                      select
                      value={mapping[dummyField] || ''}
                      onChange={(event) =>
                        handleMappingChange(dummyField, event.target.value)
                      }
                      
                      sx={{ width: '50%' }}
                    >
                      {tmpheader.map((headerOption, idx) => (
                        <MenuItem key={idx} value={headerOption}>
                          {headerOption}
                        </MenuItem>
                      ))}
                    </TextField>
                  </TableCell>
                </TableRow>
              ))
            )
            }
          </TableBody>
        </Table>
      </TableContainer>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', mt: 4 }}>
        <Button variant="text" sx={{ fontWeight: 'bold' }}
          onClick={() => setCurrentStep(1)}
        >
          BACK
        </Button>
        <Button variant="contained" color="primary"
          onClick={() => handleNext()}
        >
          NEXT
        </Button>
      </Box>
    </Paper>
  );
}
</file>

<file path="src/DataPageComponents/ImportDataComponents/SelectDataSource.js">
import React, { useState } from 'react';
import {
  Box,
  Typography,
  Paper,
  Button,
  FormControlLabel,
  Grid,
  Radio,
  RadioGroup,
  Link,
} from '@mui/material';

export default function SelectDataSource({setCurrentStep, selectedFormat, setSelectedFormat}) {

  const handleFormatChange = (event) => {
    setSelectedFormat(event.target.value);
  };

  const handleNext = () => {
    if (selectedFormat == null){
        alert("Please select data format");
        return
    }
    setCurrentStep(1)
  }

  const handleBack = () => {
    setSelectedFormat(null)
    setCurrentStep(0)
  }

  return (
    <Paper sx={{ padding: 4, display: 'flex', flexDirection: 'column', height: '80%' }}>
        <Box  sx={{ flexGrow: 1 }}>
            <Typography variant="h6" sx={{ textAlign: 'center', mt: 4, mb: 4 }}>
                Select data format
            </Typography>
            <RadioGroup
                value={selectedFormat}
                onChange={handleFormatChange}
                row
                sx={{ justifyContent: 'center' }}
            >
                <Grid container spacing={8} justifyContent="center">
                <Grid item>
                    <FormControlLabel
                    control={<Radio />}
                    label="CSV"
                    value="csv"
                    />
                </Grid>
                <Grid item>
                    <FormControlLabel
                    control={<Radio disabled />}
                    label="Image (soon)"
                    value="image"
                    />
                </Grid>
                <Grid item>
                    <FormControlLabel
                    control={<Radio disabled />}
                    label="Video (soon)"
                    value="video"
                    />
                </Grid>
                <Grid item>
                    <FormControlLabel
                    control={<Radio disabled />}
                    label="Other?"
                    value="other"
                    />
                </Grid>
                </Grid>
            </RadioGroup>
      </Box>
      <Box sx={{ display: 'flex', justifyContent: 'flex-end', mt: 4 }}>
       
          <Button variant="text" sx={{ fontWeight: 'bold', mr:4}}
            onClick={() => handleBack()}
            href="/Dashboard/Data/DataLibrary/AddData" 
          >
            BACK
          </Button>
       
        <Button variant="contained" color="primary"
            onClick={() => handleNext()}
        >
          NEXT
        </Button>
      </Box>
    </Paper>
  );
}
</file>

<file path="src/DataPageComponents/ImportDataComponents/UploadData.js">
import React, { useState, useCallback } from 'react';
import {
  Box,
  Typography,
  Paper,
  Button,
  TextField,
  MenuItem,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
  Table,
  TableCell,
  TableContainer,
  TableBody,
  TableRow,
  TableHead,
} from '@mui/material';
import { DatePicker } from '@mui/x-date-pickers'
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { useDropzone } from "react-dropzone";



  
export default function UploadData({
  setCurrentStep, 
  selectedDate, 
  setSelectedDate, 
  selectedDataOption,
  setSelectedDataOption,
  userDataList,
  filename,
  setFilename,
  tmpheader,
  setTmpheader,
  tmpdata,
  setTmpdata,
  fullHeader,
  setFullHeader,
  file,
  setFile,

}) {

  const [showData, setShowData] = useState(false);

  const handleSelectDataOption = (event) => {
    const selectedItem = userDataList.find(item => item.name === event.target.value);
    setSelectedDataOption(selectedItem);
  };


  

    /* Drag and Drop area */
    const onDrop = useCallback((acceptedFiles) => {
      acceptedFiles.map((file) => {
          uploadFiles(file, file.name, "File uploaded")
      });
  }, []);
  const { getRootProps, getInputProps, acceptedFiles, isDragActive } = useDropzone({ onDrop, accept: {'text/csv': ['.csv']} })

  /* Storage upload functions */
  function uploadFiles(file, name, method) {
      console.log(file)
      setFilename(name)
      setFile(file)
      const reader = new FileReader()

      reader.onload = function (e) {
        const text = e.target.result;
        const Data = csvToArray(text);
        setTmpdata(Data)
      };
      reader.readAsText(file)
      
      setShowData(true)

  }

  function csvToArray(str, delimiter = ",") {
      const headers = str.slice(0, str.indexOf("\n")).split(delimiter);
      setFullHeader(headers)
      console.log(fullHeader)
      if (headers.length > 10) {
        const res = headers.slice(0, 10)
        setTmpheader(res)
      } else {
        setTmpheader(headers)
      }
      const rows = str.slice(str.indexOf("\n") + 1).split("\n");
      const arr = rows.map(function (row) {
        const values = row.split(delimiter);
        const el = headers.reduce(function (object, header, index) {
          object[header] = values[index];
          return object;
        }, {});
        return el;
      });

      if (arr.length > 100) {
        return arr.slice(0, 100)
      } else {
        return arr
      }
      return 
  }

const handleNext = () => {
  if (selectedDate == null || selectedDataOption == null || file == null){
      alert("Please upload file and fill in required fields");
      return
  }
  setCurrentStep(2)
}


  return (
    <Paper sx={{ padding: 4, display: 'flex', flexDirection: 'column', height: '80%' , }}>
      <Box  sx={{ flexGrow: 1, flexDirection: 'column', justifyContent: 'center', alignItems: 'center' }}>
      <Typography variant="h6" sx={{ textAlign: 'center', mb: 4 }}>
        Upload data
      </Typography>

      <Box sx={{ mt: 2 }}>
        <Box sx={{ border: 2, borderStyle: 'dotted' }}>
            <Box {...getRootProps({})} display="flex" justifyContent="center" alignItems="center" sx={{ minHeight: 250}}>
                <input {...getInputProps()} onDrop={onDrop}/>
                {isDragActive ? (
                    <Typography variant="h5">Drop (only .csv file)</Typography>
                ) : (
                    <Typography variant="h5">Drag file and drop here / Click to upload</Typography>
                )}
            </Box>
        </Box>
      </Box>
      <Dialog open={showData} maxWidth={"lg"} fullWidth={true}>
        <DialogTitle>Data Check</DialogTitle>
        <DialogContent>
            <DialogContentText>
                Can check part content of your file below
            </DialogContentText>
            
            <Box>
                <TableContainer component={Paper} sx={{ mt: 2 }}>
                    <Table
                    sx={{ minWidth: 650 }}
                    size="small"
                    aria-label="a dense table"
                    >
                    <TableHead>
                        <TableRow>
                        {tmpheader?.map((column) => (
                            <TableCell align="right">{column}</TableCell>
                        ))}
                        </TableRow>
                    </TableHead>

                    <TableBody>
                        {tmpdata?.map((row) => (
                        <TableRow
                            key={Object.values(row)[0]}
                            sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
                        >
                            <TableCell component="th" scope="row">
                            {Object.values(row)[0]}
                            </TableCell>
                            <TableCell align="right">{Object.values(row)[1]}</TableCell>
                            <TableCell align="right">{Object.values(row)[2]}</TableCell>
                            <TableCell align="right">{Object.values(row)[3]}</TableCell>
                            <TableCell align="right">{Object.values(row)[4]}</TableCell>
                            <TableCell align="right">{Object.values(row)[5]}</TableCell>
                            <TableCell align="right">{Object.values(row)[6]}</TableCell>
                            <TableCell align="right">{Object.values(row)[7]}</TableCell>
                            <TableCell align="right">{Object.values(row)[8]}</TableCell>
                            <TableCell align="right">{Object.values(row)[9]}</TableCell>
                        </TableRow>
                        ))}
                    </TableBody>
                    </Table>
                </TableContainer>
            </Box>
        </DialogContent>

        <DialogActions>
           <Button onClick={() => setShowData(false)}>OK</Button> 
        </DialogActions>
    </Dialog>

      <Box sx={{ 
        mt:4,
        mb: 2,   
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',}}>
        <Typography variant="body1" sx={{ mb: 1, mr:8 }}>
          Choose date when data is collected
        </Typography>
        <LocalizationProvider dateAdapter={AdapterDayjs}>
        <DatePicker
          value={selectedDate}
          onChange={(newDate) => setSelectedDate(newDate)}
        />
        </LocalizationProvider>

      </Box>

      <Box sx={{ mb: 4, display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',}}>
        <Typography variant="body1" sx={{ mb: 1, mr:12, width:'220px' }}>
          Choose the data option
        </Typography>
        <TextField
          select
          value={selectedDataOption.name}
          onChange={handleSelectDataOption}
          sx={{ width: '230px' }}
        >
          {userDataList.map((item, index) => (
          <MenuItem key={index} value={item.name}>{item.name}</MenuItem>
          ))}
         
        </TextField>
      </Box>
      </Box>

      <Box sx={{ display: 'flex', justifyContent: 'space-between', mt: 4 }}>
        <Button variant="text" sx={{ fontWeight: 'bold' }}
          onClick={() => setCurrentStep(0)}
        >
          BACK
        </Button>
        <Button variant="contained" color="primary"
          onClick={() => handleNext()}
        >
          NEXT
        </Button>
      </Box>
    </Paper>
  );
}
</file>

<file path="src/DataPageComponents/ImportDataPage.js">
import React, { useState, useEffect } from 'react';
import {
  Box,
  Typography,
  Stepper,
  Step,
  StepLabel,
} from '@mui/material';
import { Link } from 'react-router-dom';
import SelectDataSource from './ImportDataComponents/SelectDataSource';
import UploadData from './ImportDataComponents/UploadData';
import DataMapping from './ImportDataComponents/DataMapping';
import firebaseApp from '../firebase-config';
import { getFirestore, doc, collection, onSnapshot, orderBy, limit, query, where, addDoc } from 'firebase/firestore'
import FinishImport from './FinishImport';

const firestore = getFirestore(firebaseApp);
const user_email = window.localStorage.getItem('user_email');

export default function ImportDataPage() {

  const steps = [ 'Select Data Format', 'Data Upload', '[Third party]', 'Finish'];

  const [currentStep, setCurrentStep] = useState(0);
  const [selectedFormat, setSelectedFormat] = useState();
  const [selectedDate, setSelectedDate] = useState(null);
  const [selectedDataOption, setSelectedDataOption] = useState('');
  const [userDataList, setUserDataList] = useState([]);
  const [filename, setFilename] = useState([]);
  const [tmpheader, setTmpheader] = useState([]);
  const [tmpdata, setTmpdata] = useState([]);
  const [fullHeader, setFullHeader] = useState([]);
  const [file, setFile] = useState(null);
  const [mapping, setMapping] = useState({});

  useEffect(() => {
    const userDataQuery = query(
        collection(firestore, 'userData'),
        where('user_email', '==', user_email),

        where('selected', '==', true),
    );

    const unsubscribe = onSnapshot(userDataQuery, snapshot => {
            let userData = snapshot.docs.map(doc => doc.data());
        
            setUserDataList(userData);
            setSelectedDataOption(userData[1])
        })

        return () => {
        unsubscribe()
        }
    }, []);

  return (
    <Box sx={{ display: 'flex', height: '100vh' }}>

      {/* Main Content */}
      <Box sx={{ flexGrow: 1, padding: 4 }}>
      <Typography variant="h6" sx={{ mb: 8,  }}>
            <Link to="/Dashboard/Data/DataLibrary" style={{ textDecoration: 'underline', color: 'inherit', fontWeight: 'bold' }}>
            Data Library
            </Link>
            {' / '}
            <Link to="/Dashboard/Data/DataLibrary/AddData" style={{ textDecoration: 'underline', color: 'inherit', fontWeight: 'bold' }}>
            Add Data
            </Link>
            {' / '}
            <span style={{ color: 'gray' }}>Import Data</span>
        </Typography>
        {/* Stepper */}
        <Stepper activeStep={currentStep} sx={{ mb: 4 }}>
          {steps.map((label, index) => (
            <Step key={index}>
              <StepLabel>{label}</StepLabel>
            </Step>
          ))}
        </Stepper>
          {currentStep == 0 &&
            <SelectDataSource 
            setCurrentStep={setCurrentStep}
            selectedFormat={selectedFormat}
            setSelectedFormat={setSelectedFormat}
            /> 
            }
        {currentStep == 1 &&
          <UploadData setCurrentStep={setCurrentStep} 
          selectedDate = {selectedDate}
          setSelectedDate = {setSelectedDate}
          selectedDataOption = {selectedDataOption}
          setSelectedDataOption = {setSelectedDataOption}
          userDataList = {userDataList}
          filename = {filename}
          setFilename = {setFilename}
          tmpheader = {tmpheader}
          setTmpheader = {setTmpheader}
          tmpdata = {tmpdata}
          setTmpdata = {setTmpdata}
          fullHeader = {fullHeader}
          setFullHeader = {setFullHeader}
          file = {file}
          setFile = {setFile}
          />
        }

        {currentStep == 2 && 
        <DataMapping 
            setCurrentStep = {setCurrentStep} 
            selectedDataOption = {selectedDataOption} 
            tmpheader = {tmpheader}
            mapping = {mapping}
            setMapping = {setMapping}
            selectedFormat = {selectedFormat}
            selectedDate = {selectedDate}
            filename = {filename}
            file = {file}
            />
        }

        {currentStep == 3 && 
        <FinishImport datasource={"Import"}/>
        }
      </Box>
    </Box>
  );
}
</file>

<file path="src/DataPageComponents/ManualInputComponents/ManualDataEntryTable.js">
import React, [Third party], useState } from 'react';
import {
  Box,
  Button,
  IconButton,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  TextField,
  Typography,
} from '@mui/material';
import { DatePicker } from '@mui/x-date-pickers'
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import dayjs from 'dayjs';
import RemoveCircleOutlineIcon from '@mui/icons-material/RemoveCircleOutline';

export default function ManualDataEntryTable({ selectedUserData, dataEntries, setDataEntries, fields }) {
  const { dummyFields } = selectedUserData; // Extract dummyFields from selectedUserData
  
  useEffect(() => {
    setDataEntries([{ ...fields.reduce((acc, field) => ({ ...acc, [field]: '' }), {}) }])

  }, [selectedUserData])

  const handleInputChange = (index, field, value) => {
    const updatedEntries = [...dataEntries];
    updatedEntries[index][field] = value;
    setDataEntries(updatedEntries);
    console.log(updatedEntries);
  };

  const handleAddRow = () => {
    setDataEntries([...dataEntries, { ...fields.reduce((acc, field) => ({ ...acc, [field]: '' }), {}) }]);
    console.log(dataEntries);
  };

  const handleRemoveRow = (index) => {
    const updatedEntries = dataEntries.filter((_, i) => i !== index);
    setDataEntries(updatedEntries);
    console.log(updatedEntries);
  };

  return (
    <Box>
      <Typography variant="h6" sx={{ mb: 2 }}>
      {selectedUserData.name}
      </Typography>
      <TableContainer>
        <Table>
          <TableHead>
            <TableRow>
              {fields.map((field, index) => (
                <TableCell key={index}><strong>{field}</strong></TableCell>
              ))}
              <TableCell></TableCell> {/* For the remove button */}
            </TableRow>
          </TableHead>
          <TableBody>
            {dataEntries.map((entry, rowIndex) => (
              <TableRow key={rowIndex}>
                {fields.map((field, index) => (
                  <TableCell key={index}>
                    {field === 'Date' || field === 'date'? (
                      <LocalizationProvider dateAdapter={AdapterDayjs}>
                      <DatePicker
                        value={entry[field] ? dayjs(entry[field]) : null}
                        onChange={(newDate) => handleInputChange(rowIndex, field, newDate)}
                        renderInput={(params) => <TextField {...params} fullWidth />}
                      />
                    </LocalizationProvider>
                    ) : (
                      <TextField
                        value={entry[field]}
                        onChange={(e) => handleInputChange(rowIndex, field, e.target.value)}
                        fullWidth
                      />
                    )}
                  </TableCell>
                ))}
                <TableCell>
                  <IconButton color="error" onClick={() => handleRemoveRow(rowIndex)}>
                    <RemoveCircleOutlineIcon />
                  </IconButton>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
      <Box sx={{ mt: 2, display: 'flex', justifyContent: 'flex-end' }}>
        <Button onClick={handleAddRow} sx={{ color: 'blue', fontWeight: 'bold' }}>
          ADD ROW
        </Button>
      </Box>
    </Box>
  );
}
</file>

<file path="src/DataPageComponents/ManualInputPage.js">
import React, {useState, useEffect} from 'react';
import {
  Box,
  Typography,
  Button,
  Paper,
  FormControl,
  Select,
  MenuItem,
} from '@mui/material';
import ManualDataEntryTable from './ManualInputComponents/ManualDataEntryTable'
import FinishImport from './FinishImport';
import dayjs from 'dayjs';
import { Link } from 'react-router-dom';
import firebaseApp from '../firebase-config';
import { getFirestore, collection, onSnapshot, query, where, getDocs, doc, updateDoc} from 'firebase/firestore'
import { v4 as uuidv4 } from 'uuid'; 

// Connect to current firebase project
const firestore = getFirestore(firebaseApp);

export default function ManualInputPage() {
    const user_email = window.localStorage.getItem('user_email');
    const [userDataList, setUserDataList] = useState([]);
    const [selectedUserData, setSelectedUserData] = useState([]);
    const [dataEntries, setDataEntries] = useState([]);
    const [currentStep, setCurrentStep] = useState(0);
    const [user, setUser] = useState("");

    useEffect(() => {
      const userQuery = query(
          collection(firestore, 'users'),
          where('email', '==', user_email)
      );
          const unsubscribe = onSnapshot(userQuery, snapshot => {
          const user = snapshot.docs.map(doc => doc.data());
          setUser(user[0]);
          })
  
          return () => {
          unsubscribe()
          }
      }, [])
    
    useEffect(() => {
        const userDataQuery = query(
            collection(firestore, 'userData'),
            where('user_email', '==', user_email),

            where('selected', '==', true),
        );
    
        const unsubscribe = onSnapshot(userDataQuery, snapshot => {
                let userData = snapshot.docs.map(doc => doc.data());
            
                setUserDataList(userData);
                setSelectedUserData(userData[1])
            })
    
            return () => {
            unsubscribe()
            }
        }, []);
    
    const handleBack = () => {
      setDataEntries([]);
      setCurrentStep(0);
    }

    const handleConfirmInput = () => {
      const isValidEntries = validateEntries();
      if (isValidEntries){
        const formattedDataEntries = formatDateEntries();
        importDataBackupIntoFirebase(formattedDataEntries);
      }
    }

    const validateEntries = () => {
      for (let rowIndex = 0; rowIndex < dataEntries.length; rowIndex++) {
        const entry = dataEntries[rowIndex];
        for (let field in entry) {
          if (entry[field] === "") {
            alert("Please fill in all required input");
            return false;  
          }
        }
      }
      return true;  
    };

    const formatDateEntries = () => {
      const formattedEntries = dataEntries.map((entry) => {
        if (entry.Date) {
          return {
            ...entry,
            Date: dayjs(entry.Date).format('ddd MMM DD YYYY'),
            user_id: user.userId,
            id: uuidv4(),
            created_at: new Date().toLocaleDateString('en-US', {
              weekday: 'short',
              month: 'short',
              day: '2-digit',
              year: 'numeric'
          }),
            updated_at: new Date().toLocaleDateString('en-US', {
              weekday: 'short',
              month: 'short',
              day: '2-digit',
              year: 'numeric'
          }),
          };
        }
        else if (entry.date) {
          return {
            ...entry,
            created_at: new Date().toLocaleDateString('en-US', {
              weekday: 'short',
              month: 'short',
              day: '2-digit',
              year: 'numeric'
          }),
            updated_at: new Date().toLocaleDateString('en-US', {
              weekday: 'short',
              month: 'short',
              day: '2-digit',
              year: 'numeric'
          }),
            date: dayjs(entry.date).format('ddd MMM DD YYYY'),
            user_id: user.userId,
            id: uuidv4(),
          };
        }
        return entry;
      });
      console.log(formattedEntries)
      setDataEntries(formattedEntries);
      return formattedEntries
    };

    // Sample data import api call to Postgresql DB, not use for now, 
    // need further ehancement for the Google Cloud Function to fit all the data schemas
    const importDataIntoSQLDB = async (formattedDataEntries) => {
      const endpoint = 'https://us-central1-[redacted-project].cloudfunctions.net/importDummyData';
    
      try {
        const response = await fetch(endpoint, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json', 
          },
          body: JSON.stringify(formattedDataEntries), 
        });
    
        if (!response.ok) {
          alert("Network response was not ok.");
        }
    
        const result = await response.json(); 
        console.log('Data successfully sent:', result);
        importDataBackupIntoFirebase(formattedDataEntries);
      } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
        alert("Failed to upload data. Please try again.");
      }
    };

    // Import manual data input into Firestore
    const importDataBackupIntoFirebase = (formattedDataEntries) => {
      let manual_input = selectedUserData.manual_input || []; 
      let newManualInput = [...manual_input, ...formattedDataEntries];

      manual_input = newManualInput

      const q = query(collection(firestore, 'userData'), where("id", "==", selectedUserData.id));

      getDocs(q).then((querySnapshot) => {
          querySnapshot.forEach((queryDocSnapshot) => {
              // Get the document reference
              const docRef = doc(firestore, 'userData', queryDocSnapshot.id);
      
              // Update the document with the new data
              updateDoc(docRef, { manual_input, status: "On Track" })
                  .then(() => {
                      console.log("Data Backup Uploaded successfully!");
                      setCurrentStep(1)
                  })
                  .catch((error) => {
                      console.error("Error updating document: ", error);
                      alert("Failed to upload backup data. Please try again.");
                  });
          });
      }).catch((error) => {
          console.error("Error getting documents: ", error);
          alert("Failed to upload backup data. Please try again.");
      });
    }

  return (
        <Box sx={{ padding: 4 }}>
        <Typography variant="h6" sx={{ mb: 8,  }}>
            <Link to="/Dashboard/Data/DataLibrary" style={{ textDecoration: 'underline', color: 'inherit', fontWeight: 'bold' }}>
            Data Library
            </Link>
            {' / '}
            <Link to="/Dashboard/Data/DataLibrary/AddData" style={{ textDecoration: 'underline', color: 'inherit', fontWeight: 'bold' }}>
            Add Data
            </Link>
            {' / '}
            <span style={{ color: 'gray' }}>Manual Input</span>
        </Typography>
        {currentStep == 0 &&
        <div>
          <Typography variant="h5" sx={{ mb: 4, textAlign: 'center' }}>
              Required Fields
          </Typography>
      
          <Paper sx={{ padding: 4, mb: 4 }}>
              {selectedUserData.fields && (
                selectedUserData.fields.length > 0 ? (
              <ManualDataEntryTable selectedUserData = {selectedUserData} dataEntries={dataEntries} setDataEntries={setDataEntries} fields = {selectedUserData.fields}/>
                ) : 
                (
                  <ManualDataEntryTable selectedUserData = {selectedUserData} dataEntries={dataEntries} setDataEntries={setDataEntries} fields = {selectedUserData.dummyFields}/>
                )
              ) 
            }
          </Paper>
      
          <Paper sx={{ padding: 2, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <Box>
              <Typography variant="body1">Name of data</Typography>
              {selectedUserData.name && (
              <FormControl variant="standard" 
                                      sx={{  mt:1, mr:2, minWidth:200, maxWidth: 220,  }}
                                      style={{ outline: 'none', boxShadow: 'none', border: 'none' }}
                                      >
                  <Select
                  value={selectedUserData.name}
                  >

                  {userDataList.map((option) => ( 
                      <MenuItem 
                      key={option.name} 
                      value={option.name}
                      onClick={() => setSelectedUserData(option)}
                      >
                      {option.name}
                      </MenuItem>
                  ))}
                  </Select>
              </FormControl>
              )}
          </Box>
          </Paper>
          <Box sx={{ display: 'flex', justifyContent: 'space-between', mt: 4 }}>
          <Button variant="text" sx={{ fontWeight: 'bold', mr:4}}
              onClick={() => handleBack()}
              href="/Dashboard/Data/DataLibrary/AddData" 
            >
              BACK
          </Button>
          <Button variant="contained" color="primary"
            onClick={() => handleConfirmInput()}
          >
            CONFIRM INPUT
          </Button>
          </Box>
        </div>
      }
      {currentStep == 1 && 
        <FinishImport datasource={"Manual_Input"}/>
        }
    </Box>
  );
}
</file>

<file path="src/DataPageComponents/SyncDataPage.js">
import React, { useState, useEffect } from 'react';
import [Third party], Paper, Radio, Typography, FormControlLabel } from '@mui/material';
import { Link } from 'react-router-dom';
import GeotabLogo from '../pics/GeotabLogo.jpg';
import SamsaraLogo from '../pics/SamsaraLogo.jpg';
import AWSLogo from '../pics/aws_logo.png';
import AzureLogo from '../pics/AzureLogo.png';
import FinishImport from './FinishImport';
import firebaseApp from '../firebase-config';
import { getFirestore, collection, onSnapshot, query, where, getDocs, doc, updateDoc} from 'firebase/firestore'

// Connect to current firebase project
const firestore = getFirestore(firebaseApp);

export default function SyncDataPage () {
    const user_email = window.localStorage.getItem('user_email');
  const [selectedOption, setSelectedOption] = useState(null);
  const [user, setUser] = useState("");
  const [currentStep, setCurrentStep] = useState(0);

  useEffect(() => {
    const userQuery = query(
        collection(firestore, 'users'),
        where('email', '==', user_email)
    );
        const unsubscribe = onSnapshot(userQuery, snapshot => {
        const user = snapshot.docs.map(doc => doc.data());
        setUser(user[0]);
        })

        return () => {
        unsubscribe()
        }
    }, [])

  const handleChange = (event) => {
    setSelectedOption(event.target.value);
  };

  const handleBack = () => {
    setSelectedOption(null);
    setCurrentStep(0)
  }
  const handleUpdateUserAPIRecord = () => {
    if (selectedOption == null) {
      alert("Please select an API option!");
      return
    }
    let api = user.api || []
    let newApiData = [
        ...api,
       selectedOption
    ]
    
    api = newApiData

    console.log(api)

    const q = query(collection(firestore, 'users'), where('email', '==', user_email));

    getDocs(q).then((querySnapshot) => {
        querySnapshot.forEach((queryDocSnapshot) => {
            // Get the document reference
            const docRef = doc(firestore, 'users', queryDocSnapshot.id);
    
            // Update the document with the new data
            updateDoc(docRef, { api })
                .then(() => {
                    console.log("API data updated successfully!");
                    setCurrentStep(1)
                })
                .catch((error) => {
                    console.error("Error updating document: ", error);
                    alert("Failed to update api data. Please try again.");
                });
        });
    }).catch((error) => {
        console.error("Error getting documents: ", error);
        alert("Failed to update api data. Please try again.");
    });

  }

  return (
    <Box sx={{ padding: 4 }}>
    <Typography variant="h6" sx={{ mb: 8,  }}>
        <Link to="/Dashboard/Data/DataLibrary" style={{ textDecoration: 'underline', color: 'inherit', fontWeight: 'bold' }}>
        Data Library
        </Link>
        {' / '}
        <Link to="/Dashboard/Data/DataLibrary/AddData" style={{ textDecoration: 'underline', color: 'inherit', fontWeight: 'bold' }}>
        Add Data
        </Link>
        {' / '}
        <span style={{ color: 'gray' }}>Sync Data</span>
    </Typography>
      <Typography variant="h5" sx={{ mb: 4, textAlign: 'center' }}>
        Setup a sync
      </Typography>
      {currentStep == 0 && 
      <Paper elevation={3} sx={{ padding: 4, width: '100%',  height: '80%'}}>
        <Grid container spacing={4} justifyContent="center">
          <Grid item xs={12} sm={6} md={6}>
            <Paper
              sx={{ padding: 2, textAlign: 'center', border: selectedOption === 'geotab' ? '2px solid blue' : '2px solid transparent' }}
              onClick={() => setSelectedOption('geotab')}
            >
              <FormControlLabel
                value="geotab"
                control={<Radio checked={selectedOption === 'geotab'} onChange={handleChange} />}
                label={
                  <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                    <Typography>Geotab</Typography>
                    <img src={GeotabLogo} alt="Geotab" style={{  height: '50px',width: '110px', mt: 8 }} />
                  </Box>
                }
                sx={{ width: '100%' }}
              />
            </Paper>
          </Grid>
          <Grid item xs={12} sm={6} md={6}>
            <Paper
              sx={{ padding: 2, textAlign: 'center', border: selectedOption === 'samsara' ? '2px solid blue' : '2px solid transparent' }}
              onClick={() => setSelectedOption('samsara')}
            >
              <FormControlLabel
                value="samsara"
                control={<Radio checked={selectedOption === 'samsara'} onChange={handleChange} />}
                label={
                  <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                    <Typography>Samsara</Typography>
                    <img src={SamsaraLogo} alt="Samsara" style={{ height: '50px',width: '130px', mt: 8 }} />
                  </Box>
                }
                sx={{ width: '100%' }}
              />
            </Paper>
          </Grid>
          <Grid item xs={12} sm={6} md={6}>
            <Paper
              sx={{ padding: 2, textAlign: 'center', border: selectedOption === 'aws' ? '2px solid blue' : '2px solid transparent' }}
              onClick={() => setSelectedOption('aws')}
            >
              <FormControlLabel
                value="aws"
                control={<Radio checked={selectedOption === 'aws'} onChange={handleChange} />}
                label={
                  <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                    <Typography>AWS</Typography>
                    <img src={AWSLogo} alt="AWS" style={{ height: '50px',width: '80px', mt: 8 }} />
                  </Box>
                }
                sx={{ width: '100%' }}
              />
            </Paper>
          </Grid>
          <Grid item xs={12} sm={6} md={6}>
            <Paper
              sx={{ padding: 2, textAlign: 'center', border: selectedOption === 'azure' ? '2px solid blue' : '2px solid transparent' }}
              onClick={() => setSelectedOption('azure')}
            >
              <FormControlLabel
                value="azure"
                control={<Radio checked={selectedOption === 'azure'} onChange={handleChange} />}
                label={
                  <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
                    <Typography>Microsoft Azure</Typography>
                    <img src={AzureLogo} alt="Azure" style={{ height: '40px',width: '130px', marginTop: 8 }} />
                  </Box>
                }
                sx={{ width: '100%' }}
              />
            </Paper>
          </Grid>
        </Grid>
      </Paper>
        }
        {currentStep == 1 && 
        <FinishImport datasource={"Sync"}/>
        }
      {/* Back and Next buttons */}
      <Box sx={{ display: 'flex', justifyContent: 'space-between', marginTop: 4 }}>
        <Button variant="text" color="primary"
        onClick={() => handleBack()}
        href="/Dashboard/Data/DataLibrary/AddData" 
        >
          BACK
        </Button>
        <Button variant="contained" color="primary"
        onClick={() => handleUpdateUserAPIRecord()}
        >
          NEXT
        </Button>
      </Box>
    </Box>
  );
};
</file>

<file path="src/EditProfileBox.js">
import * as React from 'react';
import { useState, useEffect } from "react";
import { FormControl, Box, RadioGroup, FormControlLabel, Radio, Grid, TextField, Select, 
    Button, Typography, Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle, 
    Stack} from '@mui/material';
import { getFirestore, doc, updateDoc, } from 'firebase/firestore'
import firebaseApp from './firebase-config';

// Connect to current firebase project
const firestore = getFirestore(firebaseApp);

export default function EditProfileBox({open, setOpen, user}) {
    const [firstName, setFirstName] = useState(user.firstName)
    const [lastName, setLastName] = useState(user.lastName)
    const [location, setLocation] = useState(user.location)
    const [subscriptionPlan, setSubscriptionPlan] = useState(user.subscriptionPlan)
    const [phoneNumber, setPhoneNumber] = useState(user.phoneNumber)
    const [goal, setGoal] = useState(user.goal)
    const [role, setRole] = useState(user.role)
    const user_email = window.localStorage.getItem('user_email');

    const handleClose = () => { 
        setOpen(false);
    };

    const handleSubmit = () => { 
        if (firstName == "" || lastName == "" || location == "" || phoneNumber == "" || goal == "" || role == "" ||  subscriptionPlan == "") {
            alert("Please complete all the question!")
        } else {
            let isUpgrade = false;
            if (subscriptionPlan == "Pro") {
                isUpgrade = true;
            }
            const userCredentials = {
                firstName: firstName,
                lastName: lastName,
                phoneNumber: phoneNumber,
                location: location,
                email: user_email,
                updatedAt: new Date().toISOString(),
                goal: goal,
                role: role,
                isUpgrade: isUpgrade,
                subscriptionPlan: subscriptionPlan,
            };
            
            const userRef = doc(firestore, 'users', user_email); // Assuming 'users' is the collection name
            updateDoc(userRef, userCredentials)
                .then(() => {
                    alert("Updated profile successfully!");
                    
                })
                .catch((error) => {
                    console.error("Error updating profile: ", error);
                    alert("Failed to update profile. Please try again.");
                });
            handleClose()
        }
    };

    return (
        <Dialog open={open} onClose={handleClose} maxWidth={"sm"} fullWidth={true}>
            <DialogTitle>Edit Profile</DialogTitle>
                <DialogContent>
                    <DialogContentText>
                        Edit your information:
                    </DialogContentText>
                    
                        <FormControl sx={{ ml: 4, mt: 1 }}>
                            <Box sx={{ }}>
                            <Stack direction="row" spacing={0} alignItems="center">
                                <Typography
                                    component="h1"
                                    variant="h7"
                                    noWrap
                                    sx={{ ml:2, mt:2, mr:2 }}
                                >
                                    First Name:
                                </Typography>

                                <TextField id="firstName" label={"First Name"} value={firstName} variant="standard" sx={{ ml: 5 }} onChange={(e) => setFirstName(e.target.value)}/>
                                </Stack>
                                <Stack direction="row" spacing={0} alignItems="center">
                                <Typography
                                    component="h1"
                                    variant="h7"
                                    noWrap
                                    sx={{ ml:2,  mt:2, mr:2 }}
                                >
                                    Last Name:
                                </Typography>
                                <TextField id="lastName" label="Last Name" value={lastName} variant="standard" sx={{ ml: 5 }} onChange={(e) => setLastName(e.target.value)}/>
                                </Stack>
                            </Box>

                            <Box sx={{ mt: 3 }}>
                            <Stack direction="row" spacing={0} alignItems="center">
                                <Typography
                                    component="h1"
                                    variant="h7"
                                    noWrap
                                    sx={{ ml:2,  mt:2, mr:2 }}
                                >
                                    Location:
                                </Typography>
                            <Select native defaultValue="" id="location" label="Select Location"  
                                value={location}
                                onChange={(e) => {setLocation(e.target.value)}}
                                sx= {{ml:8}}
                            >
                                <option aria-label="" value="">Location</option>
                                <option value="Canada">Canada</option>
                                <option value="Singapore">Singapore</option>
                                <option value="Hong Kong (China)">Hong Kong (China)</option>
                            </Select>
                            </Stack>
                            <Stack direction="row" spacing={0} alignItems="center">
                                <Typography
                                    component="h1"
                                    variant="h7"
                                    noWrap
                                    sx={{ ml:2,  mt:2, mr:2 }}
                                >
                                    Phone Number:
                                </Typography>
                                <TextField id="phoneNumber" label="Phone Number"  value={phoneNumber} variant="standard" sx={{ ml: 2 }} onChange={(e) => setPhoneNumber(e.target.value)}/>
                            </Stack>
                            </Box>

                            <Stack direction="row" spacing={0} alignItems="center">
                        <Typography
                            component="h1"
                            variant="h7"
                            noWrap
                            sx={{ ml: 2, mt: 2, mr:5}}
                        >
                            Subscription plan:
                        </Typography>
                            <Box display="flex" sx={{ mt: 2 }}>
                                <RadioGroup
                                    aria-labelledby="goal-radio-buttons-group-label"
                                    defaultValue={subscriptionPlan}
                                    name="goal-radio-buttons-group"
                                    onChange={(e) => setSubscriptionPlan(e.target.value)}
                                >
                                    <Grid container spacing={10}>
                                        <Grid item xs={6}>
                                            <FormControlLabel value="Basic" control={<Radio />} label="Basic" />
                                        </Grid>
                                        <Grid item xs={6}>
                                            <FormControlLabel value="Pro" control={<Radio />} label="Pro" />
                                        </Grid>
                                    </Grid>
                                </RadioGroup>
                            </Box>
                        
                        </Stack>
                        
                        <Typography
                            component="h1"
                            variant="h7"
                            noWrap
                            sx={{ ml: 2, mt: 2 }}
                        >
                            What is your main goal?
                        </Typography>

                        
                        <Box display="flex" sx={{ mt: 1, ml:5 }}>
                            <RadioGroup
                                aria-labelledby="goal-radio-buttons-group-label1"
                                defaultValue={goal}
                                name="goal-radio-buttons-group1"
                                onChange={(e) => setGoal(e.target.value)}
                            >
                                <Grid container>
                                    <Grid item xs={6}>
                                        <FormControlLabel value="Achieve regulatory requirements" control={<Radio />} label="Achieve regulatory requirements" />
                                        <FormControlLabel value="Identify new decarbonization technologies" control={<Radio />} label="Identify new decarbonization technologies" />
                                        <FormControlLabel value="Find a consultancy" control={<Radio />} label="Find a consultancy" />
                                    </Grid>
                                    <Grid item xs={6}>
                                        <FormControlLabel value="Evaluate scenarios" control={<Radio />} label="Evaluate scenarios" />
                                        <FormControlLabel value="Minimize my emissions" control={<Radio />} label="Minimize my emissions" />
                                        <FormControlLabel value="Achieve lower energy-intensity of my services" control={<Radio />} label="Achieve lower energy-intensity of my services" />
                                    </Grid>
                                </Grid>
                            </RadioGroup>
                        </Box>
                        
                        
                        <Typography
                            component="h1"
                            variant="h7"
                            noWrap
                            sx={{ ml: 2, mt: 2 }}
                        >
                            What is your role?
                        </Typography>

                        
                                <RadioGroup
                                    aria-labelledby="roal-radio-buttons-group-label"
                                    defaultValue={role}
                                    name="roal-radio-buttons-group"
                                    onChange={(e) => setRole(e.target.value)}
                                    sx={{ ml: 3, mt: 1 }}
                                >
                                    
                                    <Grid item xs={6}>
                                    <FormControlLabel value="Finance" control={<Radio />} label="Finance" />
                                    <FormControlLabel value="Marketing" control={<Radio />} label="Marketing" />
                                    
                                    
                                    <FormControlLabel value="Operations" control={<Radio />} label="Operations" />
                                    <FormControlLabel value="Development" control={<Radio />} label="Development" />
                                    
                                    </Grid>
                                </RadioGroup>
                        </FormControl>                  
                </DialogContent>
            
            <DialogActions>
                <Button onClick={handleClose}>Cancel</Button>
                <Button onClick={handleSubmit}>Submit</Button>
            </DialogActions>
        </Dialog>
    )
}
</file>

<file path="src/FinancePage.js">
import * as React from 'react';
import { useState } from "react";
import Box from '@mui/material/Box';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Container from '@mui/material/Container';
import Paper from '@mui/material/Paper';
import { styled } from '@mui/material/styles';
import PlanningPage from './FinancePageComponents/PlanningPage';
import DataSelectionPage from './FinancePageComponents/DataSelectionPage';
import GoalMetricsPage from './FinancePageComponents/GoalMetricsPage';
import ActionPlanPage from './FinancePageComponents/ActionPlanPage';

// Connect to current firebase project

export default function FinancePage({ selectedTab }) {
  const [value, setValue] = useState(selectedTab);
  const handleChange = (event, newValue) => {
    setValue(newValue);
  }

  // StyledTab component with custom styles
    const StyledTab = styled(Tab)(({ theme, selected }) => ({
        minWidth: 0, // Allow the tab to shrink
        flex: 1, // Flexible width
        whiteSpace: 'normal', // Allow text to wrap to the next line
        border: '1px solid #CCCCCC', // Border style
        backgroundColor: selected ? '#CCCCCC' : 'inherit', // Grey background when selected
        color: selected ? '#000000' : '#000000', // Black text when selected
        '&:hover': {
          backgroundColor: '#CCCCCC', // Grey background on hover
        },
        fontWeight: 'bold', // Bold text
    }));

      // Function to render content based on the selected tab
    const renderTabContent = (tabIndex) => {
        switch (tabIndex) {
        case 0:
          return <PlanningPage />;
        case 1:
          return <GoalMetricsPage/>;
            
        case 2:
          return <DataSelectionPage/>
        case 3:
          return <ActionPlanPage/>;
        default:
          return null;
        }
    };

  return (
    <Container maxWidth="lg" sx={{ mt: 2, ml:3, mr:5, mb: 4 }}>
    <Box sx={{ width: '100%' }}>
      <Tabs 
        value={value} 
        onChange={handleChange} 
        aria-label="Finance Menu"
      >
        <StyledTab label="Planning" href="/Dashboard/Finance/Planning" />
        <StyledTab label="Goal Metrics" href="/Dashboard/Finance/GoalMetrics" />
        <StyledTab label="Data Selection (Coming Soon)" href="/Dashboard/Finance/DataSelection" disabled/>
        <StyledTab label="Action Plan (Coming Soon)" href="/Dashboard/Finance/ActionPlans" disabled />
        <StyledTab label="Acounting (Coming Soon)" disabled />
        <StyledTab label="Tax & Compliance (Coming Soon)" disabled />
      </Tabs>
      <Paper sx={{ display: 'flex', width: '100%', height: '100%',  mb: 2 }}>
       {/* Render content based on the selected tab */}
       {renderTabContent(value)}
      </Paper>
      
    </Box>
    </Container>
  );
};
</file>

<file path="src/FinancePageComponents/ActionPlanPage.js">
import * as React from 'react';
import { useState, useEffect } from "react";
import Box from '@mui/material/Box';
import ListItem from '@mui/material/ListItem';
import Typography from '@mui/material/Typography';

export default function ActionPlanPage() {
    return (
            
        <Box sx={{ flexGrow: 1, maxWidth: 1504, bgcolor: '#D9D9D9'}}>
            <ListItem>
                <Typography
                    component="h1"
                    variant="h6"
                    color="inherit"
                    noWrap
                    sx={{ flexGrow: 1,fontWeight: 'bold', mt:2, ml:2, mr: 3 }}
                >
                    Financial Plan
                </Typography>

            </ListItem>
        </Box>
    );
}
</file>

<file path="src/FinancePageComponents/DataSelectionPage.js">
import * as React from 'react';
import { useState, useEffect } from "react";
import Box from '@mui/material/Box';
import ListItem from '@mui/material/ListItem';
import Typography from '@mui/material/Typography';

export default function DataSelectionPage() {
    return (
            
        <Box sx={{ flexGrow: 1, maxWidth: 1504, bgcolor: '#FAFAFA'}}>
            <ListItem>

            </ListItem>
        </Box>
    );
}
</file>

<file path="src/FinancePageComponents/EditMetricBox.js">
import * as React from 'react';
import { useState, useEffect } from "react";
import { FormControl, Table, TableContainer, TableCell, TableBody, TableHead, TextField, TableRow, 
    Button, Typography, Dialog, DialogActions, DialogContent, Paper, DialogTitle, 
    Stack} from '@mui/material';
import { DatePicker } from '@mui/x-date-pickers'
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { getFirestore, doc, updateDoc, query, collection, getDocs, where, limit, orderBy, onSnapshot,addDoc} from 'firebase/firestore'
import firebaseApp from '../firebase-config';
import dayjs from 'dayjs';

// Connect to current firebase project
const firestore = getFirestore(firebaseApp);

export default function EditMetricBox({editMetricOpen, setEditMetricOpen, data, location, action}) {
    const [metricValue, setMetricValue] = useState([]);
    const [metricType, setMetricType] = useState([]);
    const [editedValues, setEditedValues] = useState([]);
    const [rows, setRows] = useState([
        { amount: '', time: dayjs() }
    ]);
    const [ID, setID] = useState("");
    const user_email = window.localStorage.getItem('user_email');
    const industry = window.localStorage.getItem('industry');

    useEffect(() => {
        if(data.metricValue) {
        setMetricValue(data.metricValue);
        }
        setMetricType(data.type)
    }, [data]);

    // Get user data max ID for later new created user date document Id assignment
    useEffect(() => {
        const idQuery = query(
            collection(firestore, 'userMetrics'),
            limit(1),
            orderBy('id', 'desc')
        );
        onSnapshot(idQuery, snapshot => {
            const t = (snapshot.docs.map(doc => ({ id: doc.data().id })))
            if (!t[0]) {
                setID(0)
                
            } else {
                setID(JSON.stringify(t[0].id))
            }
        })
    }, [])

    const handleClose = () => { 
        setEditMetricOpen(false);
        setEditedValues([]);
        setRows([
            { amount: '', time: dayjs() }
        ]);
    };

    const handleSubmit = () => { 
        let value = [];
        if (metricValue == []) {
            alert("Please fill in the metric value!")
        } else {
            if (metricType == "Operational"){
            value = metricValue
            }
            else{
                value = combineValues();
            }

            const q = query(collection(firestore, 'userMetrics'), where("id", "==", data.userMetricsId));
            
            getDocs(q).then((querySnapshot) => {
                querySnapshot.forEach((queryDocSnapshot) => {
                    // Get the document reference
                    const docRef = doc(firestore, 'userMetrics', queryDocSnapshot.id);
            
                    // Update the document with the new data
                    updateDoc(docRef, { value })
                        .then(() => {
                            alert("Metric value updated successfully!");
                        })
                        .catch((error) => {
                            console.error("Error updating document: ", error);
                            alert("Failed to update metric value. Please try again.");
                        });
                });
            }).catch((error) => {
                console.error("Error getting documents: ", error);
                alert("Failed to update metric value. Please try again.");
            });

        
            setEditMetricOpen(false);
    };
    }

    const handleAddMetricSubmit = () => { 
        let value = [];
        if (metricValue == []) {
            alert("Please fill in the metric value!")
        } else {
            if (metricType == "Operational"){
            value = metricValue
            }
            else{
                
                value = combineAddedValues();
                console.log(value)
            }

            let id = Number(ID) + 1 
            
            setID(id)
            
            const metricsData = {
                id: id,
                metricsId: data.metricsId,
                metricsName: data.name,
                type: data.type,
                unit: data.unit,
                value: value,
                location: location,
                dataEdit: new Date(),
                industry: industry,
                user_email: user_email,
               
            }
            addDoc(collection(firestore, 'userMetrics'), metricsData);
            alert("You have sucessfully added the metrics!")
            setEditMetricOpen(false);
    };
    }


    const handleEdit = (index, field, newValue) => {
        const updatedValues = [...editedValues];
        updatedValues[index] = { ...updatedValues[index], [field]: newValue };
        setEditedValues(updatedValues);
    };

    const handleNewRowEdit = (index, field, value) => {
        const newRows = [...rows];
        newRows[index] = { ...newRows[index], [field]: value };
        setRows(newRows);
    };

    const addRow = () => {
        setRows([...rows, { amount: '', time: dayjs() }]);
    };

    const combineValues = () => {
        const finalObjects = metricValue.map((value, index) => {
            const editedAmount = editedValues[index]?.amount ?? value.amount;
            const editedTime = editedValues[index]?.time ? editedValues[index].time.format('ddd MMM DD YYYY') : value.time;
            
            return {
                amount: editedAmount,
                time: editedTime
            };
        });
        
        return finalObjects;
    };

    const combineAddedValues = () => {
        const finalObjects = rows.map((value, index) => {
            const amount = rows[index].amount 
            const time = rows[index].time.format('ddd MMM DD YYYY')
            
            return {
                amount: amount,
                time: time
            };
        });
        
        return finalObjects;
    };


    return (
        <Dialog open={editMetricOpen} onClose={handleClose} maxWidth={"sm"} fullWidth={true}>
            {action == "Edit" ?(
            <div>
            <DialogTitle>Edit Metric Value</DialogTitle>
                <DialogContent>
                    
                        <FormControl sx={{ ml: 4, mt: 1 }}>
                           { metricType == "Operational" ? (
                            <Stack direction="row" spacing={0} alignItems="center">
                                <Typography
                                    component="h1"
                                    variant="h7"
                                    noWrap
                                    sx={{ ml:2, mt:2, mr:2 }}
                                >
                                    Metric Value:
                                </Typography>

                                <TextField id="metricValue" label={"Metric Value"} value={metricValue} variant="standard" sx={{ ml: 5 }} onChange={(e) => setMetricValue(e.target.value)}/>
                                </Stack>
                           ) : (
                            <>
                            <Typography
                                    component="h1"
                                    variant="h7"
                                    noWrap
                                    sx={{ ml:2, mt:2, mr:2 }}
                                >
                                    Metric Value:
                            </Typography>
                           
                                 <TableContainer component={Paper}>
                                 <Table>
                                     <TableHead>
                                         <TableRow>
                                             <TableCell>Amount</TableCell>
                                             <TableCell>Time</TableCell>
                                         </TableRow>
                                     </TableHead>
                                     <TableBody>
                                    {metricValue && 
                                    metricValue.map((value, index) => (
                                        <TableRow key={index}>
                                            <TableCell>
                                                <TextField
                                                    value={editedValues[index]?.amount !== undefined ? editedValues[index]?.amount : value.amount}
                                                    onChange={(e) => handleEdit(index, 'amount', e.target.value)}
                                                />
                                            </TableCell>
                                            <TableCell>
                                                <LocalizationProvider dateAdapter={AdapterDayjs}>
                                                    <DatePicker
                                                        value={editedValues[index]?.time !== undefined ? editedValues[index]?.time : dayjs(value.time)}
                                                        onChange={(date) => handleEdit(index, 'time', date)}
                                                    />
                                                </LocalizationProvider>
                                            </TableCell>
                                        </TableRow>
                                    ))}
                                     </TableBody>
                                 </Table>
                             </TableContainer>
                            </>
                           )}
                        </FormControl>                  
                </DialogContent>
            
            <DialogActions>
                <Button onClick={handleClose}>Cancel</Button>
                <Button onClick={handleSubmit}>Submit</Button>
            </DialogActions>
            </div>
        ):(
            <div>
            <DialogTitle>Add Metric Value</DialogTitle>
                <DialogContent>
                    
                        <FormControl sx={{ ml: 4, mt: 1 }}>
                           { metricType == "Operational" ? (
                            <Stack direction="row" spacing={0} alignItems="center">
                                <Typography
                                    component="h1"
                                    variant="h7"
                                    noWrap
                                    sx={{ ml:2, mt:2, mr:2 }}
                                >
                                    Metric Value:
                                </Typography>

                                <TextField id="metricValue" label={"Metric Value"} value={metricValue} variant="standard" sx={{ ml: 5 }} onChange={(e) => setMetricValue(e.target.value)}/>
                                </Stack>
                           ) : (
                            <>
                            <Typography
                                    component="h1"
                                    variant="h7"
                                    noWrap
                                    sx={{ ml:2, mt:2, mr:2 }}
                                >
                                    Metric Value:
                            </Typography>
                           
                                 <TableContainer component={Paper}>
                                 <Table>
                                     <TableHead>
                                         <TableRow>
                                             <TableCell>Amount</TableCell>
                                             <TableCell>Time</TableCell>
                                         </TableRow>
                                     </TableHead>
                                     <TableBody>
                                   
            {rows.map((row, index) => (
                <TableRow key={index}>
                    <TableCell>
                        <TextField
                            value={row.amount}
                            onChange={(e) => handleNewRowEdit(index, 'amount', e.target.value)}
                        />
                    </TableCell>
                    <TableCell>
                        <LocalizationProvider dateAdapter={AdapterDayjs}>
                            <DatePicker
                                value={row.time}
                                onChange={(date) => handleNewRowEdit(index, 'time', date)}
                            />
                        </LocalizationProvider>
                    </TableCell>
                </TableRow>
            ))}
            <Button onClick={addRow}>Add Row</Button>
        
                                     </TableBody>
                                 </Table>
                             </TableContainer>
                            </>
                           )}
                        </FormControl>                  
                </DialogContent>
            
            <DialogActions>
                <Button onClick={handleClose}>Cancel</Button>
                <Button onClick={handleAddMetricSubmit}>Submit</Button>
            </DialogActions>
            </div>
        )}
        </Dialog>
    )

}
</file>

<file path="src/FinancePageComponents/GoalMetricsComponents/GoalMetricsDetailBox.js">
import * as React from 'react';
import { useState, useEffect } from "react";
import {Typography, Paper, Stack, Avatar, Button, List, ListItem, ListItemText} from '@mui/material';


export default function GoalMetricsDetailBox(props) {
    const selectedItem = props.selectedItem
    const userDataList = props.userDataList
    const selectedItemStatus = props.selectedItemStatus
    const [selectedItemDatasource, setSelectedItemDatasource] = useState([]);
    const [selectedItemSensorData, setSelectedItemSensorData] = useState([]);


    useEffect(() => {
        console.log(selectedItemStatus)
        let datasource = userDataList.filter((item) =>
            selectedItem.datasource.includes(item.name)
          )
        setSelectedItemDatasource(datasource);

        let sensorData = userDataList.filter((item) =>
            selectedItem.sensorFieldData.includes(item.name)
          )
        setSelectedItemSensorData(sensorData);
        

    }, [selectedItem, userDataList])
        
    return (
            <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column', height: '100%', mr: 6, bgcolor: '#D9D9D9'}}>
                <Stack direction="row" spacing={0} alignItems="center">
                    <Typography
                        component="h1"
                        variant="h7"
                        color="inherit"
                        noWrap
                        sx={{ flexGrow: 1, ml: 1, mb: 1, fontWeight: 'bold' }}
                    >
                        {selectedItem.name}
                    </Typography>
                    <Typography
                        component="h1"
                        variant="h7"
                        color="inherit"
                        noWrap
                        sx={{
                            flexGrow: 1,
                            mt: -1,
                            textAlign: 'center',
                            backgroundColor: '#E0EDFB',
                            padding: '1px 1px',
                        }}
                    >
                        {selectedItem.tech}
                    </Typography>
                    {selectedItem.type === 'Operational' || selectedItem.type === 'Financial' ? (
                        <Avatar
                            sx={{ width: 50, height: 50, alignSelf: 'center', ml: 4 }}
                        >
                            {selectedItem.type === 'Operational' ? 'OP' : 'FI'}
                        </Avatar>
                    ) : null}
                    
                </Stack>
                <Stack direction="column" spacing={0} >
                    <Typography
                            component="h1"
                            variant="h7"
                            color="inherit"
                            wrap
                            sx={{  ml: 1}}
                        >
                            Description
                    </Typography>
                    
                        <Typography
                        component="h1"
                        variant="body1"
                        color="#707070"
                        sx={{ ml: 1, mb: 1,}}
                        >
                        {selectedItem.description}
                        </Typography>
                    
                    
                </Stack>
                <Stack direction="column" spacing={0} >
                <Stack direction="row" spacing={0} alignItems="center" sx={{ ml:1, justifyContent: 'space-between', borderTop: '2px solid white', paddingTop: 1 }}>
                    <Typography
                        component="h1"
                        variant="h7"
                        color="inherit"
                        wrap
                    >
                        Data Source
                    </Typography>
                    {selectedItemStatus == "selected" &&
                    <Button 
                    variant="h7" 
                    sx={{ bgcolor: '#DEDEDE', boxShadow: '0px 2px 4px rgba(0, 0, 0, 0.1)' }}
                    href="/Dashboard/Data/DataLibrary/AddData" 
                    >
                        + ADD DATA
                    </Button>
                    }
                </Stack>
                
                {selectedItemStatus == "selected" ? (
                <List sx={{ ml: 1}}>
                        {selectedItemDatasource.map((row) => (
                            <ListItem sx={{ mt: -2, mb: -1 }}
                                secondaryAction={
                                    <ListItemText
                                    primary={row.status}
                                    sx={{
                                        color: row.status == 'On Track' ? 'green' : 'red',
                                        fontWeight: 'bold',
                                    }}
                                    />
                                }
                            >
                                <ListItemText
                                    primary={row.name}
                                    sx={{color:"#707070"}}
                                />
                            </ListItem>
                    
                        ))}
                    </List>
                ):(
                    <List sx={{ ml: 1}}>
                        {selectedItem.datasource.map((data) => (
                            <ListItem sx={{ mt: -2, mb: -1 }}>
                                <ListItemText
                                    primary={data}
                                    sx={{color:"#707070"}}
                                />
                            </ListItem>
                    
                        ))}
                    </List>
                )}
                </Stack>
                <Stack direction="column" spacing={0} >
                    <Typography
                            component="h1"
                            variant="h7"
                            color="inherit"
                            wrap
                            sx={{  ml: 1, borderTop: '2px solid white', paddingTop: 1}}
                        >
                            Sensor Field Data
                    </Typography>
                    {selectedItemStatus == "selected" ? (
                    Object.keys(selectedItemSensorData).length > 0 ? (
                    <List sx={{ ml: 1}}>
                        {selectedItemSensorData.map((row) => (
                            <ListItem sx={{ mt: -2, mb: -1 }}
                                secondaryAction={
                                    <ListItemText
                                    primary={row.status}
                                    sx={{
                                        color: row.status == 'On Track' ? 'green' : 'red',
                                        fontWeight: 'bold',
                                    }}
                                    />
                                }
                            >
                                <ListItemText
                                    primary={row.name}
                                    sx={{color:"#707070"}}
                                />
                            </ListItem>
                    
                        ))}
                    </List>
                    ):(
                        <Typography
                            component="h1"
                            variant="h7"
                            color="#707070"
                            wrap
                            sx={{  ml: 3, mb: 1}}
                        >
                            Not Applicable
                        </Typography>
                    )
                ):(
                    <List sx={{ ml: 1}}>
                        {selectedItem.sensorFieldData.map((data) => (
                            <ListItem sx={{ mt: -2, mb: -1 }}>
                                <ListItemText
                                    primary={data}
                                    sx={{color:"#707070"}}
                                />
                            </ListItem>
                    
                        ))}
                    </List>
                )}

                    
                </Stack>
                <Stack direction="column" spacing={0} >
                    <Typography
                            component="h1"
                            variant="h7"
                            color="inherit"
                            wrap
                            sx={{  ml: 1, borderTop: '2px solid white', paddingTop: 1}}
                        >
                            Methodology
                    </Typography>
                    <Typography
                        
                        component="h1"
                        variant="body1"
                        color="#707070"
                        sx={{ ml: 1, mb: 1 }}
                        >
                        Summarizes how the metric is calculated.
                    </Typography>
                    
                    <Typography
                       
                        component="h1"
                        variant="body1"
                        color="#707070"
                        sx={{ ml: 1, mb: 1 }}
                        >
                        {selectedItem.methodology}
                    </Typography>    
                </Stack>
            </Paper>
    )
}
</file>

<file path="src/FinancePageComponents/GoalMetricsPage.js">
import * as React from 'react';
import { useState, useEffect } from "react";
import Box from '@mui/material/Box';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import ListItemText from '@mui/material/ListItemText';
import Button from '@mui/material/Button';
import { Select, MenuItem, FormControl, InputLabel, Chip, Checkbox, Stack} from '@mui/material';
import AddIcon from '@mui/icons-material/Add';
import RemoveIcon from '@mui/icons-material/Remove';
import { getFirestore, collection, onSnapshot, query, limit, orderBy, where, doc, updateDoc, addDoc, getDocs } from 'firebase/firestore'
import firebaseApp  from "../firebase-config"
import GoalMetricsDetailBox from './GoalMetricsComponents/GoalMetricsDetailBox';

// Connect to current firebase project
const firestore = getFirestore(firebaseApp);

/* Identify the current user */
const user_email = window.localStorage.getItem('user_email');

export default function GoalMetricsPage() {
    const [selectedMetricList, setSelectedMetricList] = useState([]);
    const [unselectedMetricList, setUnselectedMetricList] = useState([]);
    const [filteredSelectedMetricList, setFilteredSelectedMetricList] = useState([]);
    const [filteredUnselectedMetricList, setFilteredUnselectedMetricList] = useState([]);
    const [user, setUser] = useState([]);
    const [userSelectedMetricIds, setUserSelectedMetricIds] = useState([]);
    const [userDataList, setUserDataList] = useState([]);
    const [userDataNameList, setUserDataNameList] = useState([]);
    const [selectedItem, setSelectedItem] = useState({});
    const [selectedItemStatus, setSelectedItemStatus] = useState({});
    const [selectedTypes, setSelectedTypes] = useState([]);
    const [dataOptionsList, setDataOptionsList] = useState([]);
    const [ID, setID] = useState("");
    const options = ['Financial', 'Operational'];
    const industry = window.localStorage.getItem('industry');

    /* Firestore SDK queries */
    
    // Get user Selected Metrics ID List
    useEffect(() => {
        const userQuery = query(
          collection(firestore, 'users'),
          where('email', '==', user_email)
        );
          const unsubscribe = onSnapshot(userQuery, snapshot => {
            const user = snapshot.docs.map(doc => doc.data());
            setUser(user[0]);
            setUserSelectedMetricIds(user[0].selectedMetricIds);
          })
  
          return () => {
            unsubscribe()
          }
        }, [])

    // Get all metrics list and set the selected metric list and unselected metric list base on user's Selected Metrics ID List
    useEffect(() => {
        const metricsQuery = query(
            collection(firestore, 'metrics'),
            where('industry', '==', industry),
            orderBy('id')
            );

        onSnapshot(metricsQuery, snapshot => {
            const metrics = snapshot.docs.map(doc => doc.data());
            const selectedMetrics = metrics.filter(metric => userSelectedMetricIds.includes(metric.id));
            setSelectedMetricList(selectedMetrics)
            setFilteredSelectedMetricList(selectedMetrics)
            const unselectedMetricList = metrics.filter(metric => !userSelectedMetricIds.includes(metric.id));
            setUnselectedMetricList(unselectedMetricList);
            setFilteredUnselectedMetricList(unselectedMetricList);

        })
    }, [userSelectedMetricIds]);

    // Get all data option list for reference to create user data later
    useEffect(() => {
        const dataOptionsQuery = query(
          collection(firestore, 'dataOptions'),
        );
          const unsubscribe = onSnapshot(dataOptionsQuery, snapshot => {
            const dataOptions = snapshot.docs.map(doc => doc.data());
            setDataOptionsList(dataOptions);
          })
  
          return () => {
            unsubscribe()
          }
        }, [])

    // Get esisting user data list of the user from [Third party](() => {
        const userDataQuery = query(
            collection(firestore, 'userData'),
            where('user_email', '==', user_email)
        );
    
        const unsubscribe = onSnapshot(userDataQuery, snapshot => {
             const userData = snapshot.docs.map(doc => doc.data());
             const userDataName = userData.map(item => item.name);
             setUserDataList(userData);
             setUserDataNameList(userDataName);
            })

            return () => {
            unsubscribe()
            }
        }, [])

    // Get user data max ID for later new created user date document Id assignment
    useEffect(() => {
        const idQuery = query(
            collection(firestore, 'userData'),
            limit(1),
            orderBy('id', 'desc')
        );
        onSnapshot(idQuery, snapshot => {
            const t = (snapshot.docs.map(doc => ({ id: doc.data().id })))
            if (!t[0]) {
                setID(0)
                
            } else {
                setID(JSON.stringify(t[0].id))
            }
        })
    }, [])
    
    // Control the display of the GoalMetricDetailBox
    const handleSelectedItemClick = (itemName, status) => {
        setSelectedItem(itemName); // Update selected item state
        setSelectedItemStatus(status);
      };

      const handleUnselectedItemClick = () => {
        setSelectedItem([]); // Update selected item state
      };

    // Handle the filter function of Financial or Operational
    const handleSelectedTypesChange = (event) => {
        setSelectedTypes(event.target.value);
        if (event.target.value.length > 0){
            setFilteredSelectedMetricList(
            selectedMetricList.filter((item) =>
                event.target.value.includes(item.type)
        ))
        setFilteredUnselectedMetricList(
            unselectedMetricList.filter((item) =>
                event.target.value.includes(item.type)
        ))
        }
        else{
            setFilteredSelectedMetricList(selectedMetricList)
            setFilteredUnselectedMetricList(unselectedMetricList)
        }
    };
    
    // Handle Add Metrics
    const handleAddMetrics = (row) => {
        setSelectedItem([]);
        const updatedSelectedMetricIds = [...userSelectedMetricIds];
        updatedSelectedMetricIds.push(row.id);
        createUserDataRecord(row,updatedSelectedMetricIds);
        setUserSelectedMetricIds(updatedSelectedMetricIds);
        updateSelectedMetricsRecord(updatedSelectedMetricIds);
    }

    // Handle Remove Metrics
    const handleRemoveMetrics = (row) => {
        setSelectedItem([]);
        const updatedSelectedMetricIds = userSelectedMetricIds.filter(id => id !== row.id);
       
        setUserSelectedMetricIds(updatedSelectedMetricIds);
        updateSelectedMetricsRecord(updatedSelectedMetricIds);

        const affectedDatasource = row.datasource.concat(row.sensorFieldData);

        handleDBSelectedStatusChange(affectedDatasource, false, updatedSelectedMetricIds)
        

    }
    // Update user's selected metric Id list in db
    const updateSelectedMetricsRecord = (updatedSelectedMetricIds) => {
        const userRef = doc(firestore, 'users', user_email); // Assuming 'users' is the collection name
            updateDoc(userRef, {
                selectedMetricIds: updatedSelectedMetricIds
            })
                .then(() => {
                    alert("Updated selected metrics successfully!");
                    
                })
                .catch((error) => {
                    console.error("Error updating selected metrics : ", error);
                    alert("Failed to update selected metrics. Please try again.");
                });

    }

    // Create User Data function 
    const createUserDataRecord = (row, metricIds) => {

        const requiredDatasource = row.datasource.concat(row.sensorFieldData);
        console.log("requiredDatasource")
        console.log(requiredDatasource)
       
        handleDBSelectedStatusChange(requiredDatasource, true, metricIds);
        let requiredDataOptions = dataOptionsList.filter((item) =>
            requiredDatasource.includes(item.name)
        )



        requiredDataOptions = requiredDataOptions.filter((item) =>
            !userDataNameList.includes(item.name)
        )

        let id = ID;
        const updatedRequiredDataOptions = requiredDataOptions.map((dataOption) => {
            id ++
            setID(id)
        return{
            ...dataOption,
            id: id,
            dataOptionId: dataOption.id, // Renaming the id field to dataOptionId
            status: 'Required', 
            location: user.location,
            user_email: user_email,
            manual_input: [],
            importData: [],
            sync: [],
            serviceRequest: [],
            modelIds: [],
            siteId: '',
            selected: true, // Assuming selected is a boolean field, provide initial value
            lastUpdated: new Date(),
            createdAt: new Date(),
        }
        });
        updatedRequiredDataOptions.map((data) => {
            userDataNameList.push(data.name);
            userDataList.push(data);
            addDoc(collection(firestore, 'userData'), data);
        })
       
    }

    // Update the user data selected status basing on select/unselect metric
    const handleDBSelectedStatusChange = (requiredDatasource, status, metricIds) => {
        // Change selected to true when add metric
        if (status == true){
            const updatedUserData = userDataList.map((item) => {
                if (requiredDatasource.includes(item.name)) {
                    const q = query(collection(firestore, 'userData'), where("id", "==", item.id));
                    getDocs(q).then((querySnapshot) => {
                        querySnapshot.forEach((queryDocSnapshot) => {
                            // Get the document reference
                            const docRef = doc(firestore, 'userData', queryDocSnapshot.id);
                    
                            // Update the document with the new data
                            updateDoc(docRef, { selected: true })
                                .then(() => {
                                    
                                })
                                .catch((error) => {
                                    console.error("Error updating document: ", error);
                                    
                                });
                        });
                     }).catch((error) => {
                            console.error("Error getting documents: ", error);
                            
                        });
                   
                    return {
                        ...item,
                        selected: true
                    };
                }
                return item; 
            });
            setUserDataList(updatedUserData)
        }
        // change selected to false when remove a metric
        else{
            const updatedUserData = userDataList.map((item) => {
                // check if the unselected metric contain this user data and this user data does not contain any of the selected metrics Ids
                // => set selected = false
                if (requiredDatasource.includes(item.name) && metricIds.every((id) => !item.metricIds.includes(id))) {
                    console.log("In the loop")
                    console.log(item)
                    const q = query(collection(firestore, 'userData'), where("id", "==", item.id));
                    getDocs(q).then((querySnapshot) => {
                        querySnapshot.forEach((queryDocSnapshot) => {
                            // Get the document reference
                            const docRef = doc(firestore, 'userData', queryDocSnapshot.id);
                    
                            // Update the document with the new data
                            updateDoc(docRef, { selected: false })
                                .then(() => {
                                    
                                })
                                .catch((error) => {
                                    console.error("Error updating document: ", error);
                                    
                                });
                        });
                     }).catch((error) => {
                            console.error("Error getting documents: ", error);
                            
                        });
                   
                    return {
                        ...item,
                        selected: true
                    };
                }})
            setUserDataList(updatedUserData)
        }
    }

    return (          
        <Box sx={{ flexGrow: 1, height: '100vh', maxWidth: 1504, bgcolor: '#D9D9D9'}}>
            <ListItem>
                <Typography
                    component="h1"
                    variant="h6"
                    color="inherit"
                    noWrap
                    sx={{ flexGrow: 1,fontWeight: 'bold', mt:2, ml:2, mr: 3 }}
                >
                    Goal Metrics
                </Typography>
            </ListItem>
            <FormControl sx={{ml:4, minWidth: 200 }}>
                <InputLabel id="multi-select-type-label">Label</InputLabel>
                    <Select
                        labelId="multi-select-type-label"
                        multiple
                        value={selectedTypes}
                        onChange={handleSelectedTypesChange}
                        renderValue={(selected) => (
                        <div style={{ display: 'flex', flexWrap: 'wrap' }}>
                            {selected.map((value) => (
                            <Chip key={value} 
                                label={value}     
                                style={{ margin: 2 }} />
                            ))}
                        </div>
                        )}
                        MenuProps={{
                        PaperProps: {
                            style: {
                            maxHeight: 224,
                            width: 250,
                            },
                        },
                        }}
                    >
                        {options.map((option) => (
                        <MenuItem key={option} value={option}>
                            <Checkbox checked={selectedTypes.indexOf(option) > -1} />
                            {option}
                        </MenuItem>
                        ))}
                    </Select>
            </FormControl>
            <Grid container spacing={2} ml={2} mt={2} >
                <Grid item xs={12} md={8} lg={6}>
                    <Paper sx={{ display: 'flex', flexDirection: 'column', overflow: 'auto', mr: 4, height: 600}}>
                    <List>           
                        <Typography
                            component="h1"
                            variant="h7"
                            color="inherit"
                            noWrap
                            sx={{ flexGrow: 1,fontWeight: 'bold', mt:2, ml:2, mr: 3 }}
                        >
                            Selected Metrics (Press - to remove metrics)
                        </Typography>
                            {filteredSelectedMetricList?.map((row) => (
                                <Stack direction="row" spacing={0} alignItems="center">
                                    <ListItemButton
                                        key={row.name}
                                        selected={selectedItem === row.name}
                                        onClick={() => handleSelectedItemClick(row, "selected")}
                                        sx={{
                                            backgroundColor: selectedItem === row.name ? '#D9D9D9' : 'inherit', // Grey color when selected
                                        }}
                                    >
                                        <ListItemText
                                            primary={row.name}
                                            secondary={
                                                <Typography
                                                    component="span"
                                                    variant="body2"
                                                    sx={{
                                                        bgcolor: '#E0EDFB',
                                                        padding: '2px 4px',
                                                        borderRadius: '4px',
                                                        display: 'inline-block'
                                                    }}
                                                >
                                                    {row.tech}
                                                </Typography>
                                                }
                                            sx={{
                                                display: 'flex',
                                                justifyContent: 'space-between',
                                            
                                            }}

                                        />
                                        
                                    </ListItemButton>
                                    <Button onClick={() => handleRemoveMetrics(row)} 
                                    > 
                                        <RemoveIcon />
                                    </Button>
                                </Stack>
                            ))}
                        </List>
                        <List>           
                        <Typography
                            component="h1"
                            variant="h7"
                            color="inherit"
                            noWrap
                            sx={{ flexGrow: 1,fontWeight: 'bold', mt:2, ml:2, mr: 3 }}
                        >
                            Unselected Metrics (Press + to add metrics)
                        </Typography>
                            {filteredUnselectedMetricList?.map((row) => (
                                <Stack direction="row" spacing={0} alignItems="center">
                                    <ListItemButton
                                        key={row.name}
                                        selected={selectedItem === row.name}
                                        onClick={() => handleSelectedItemClick(row, "unselected")}
                                        sx={{
                                            
                                            backgroundColor: selectedItem === row.name ? '#D9D9D9' : 'inherit', // Grey color when selected
                                        }}
                                    >
                                        <ListItemText
                                            primary={row.name}
                                            secondary={
                                                <Typography
                                                    component="span"
                                                    variant="body2"
                                                    sx={{
                                                        bgcolor: '#E0EDFB',
                                                        padding: '2px 4px',
                                                        borderRadius: '4px',
                                                        display: 'inline-block'
                                                    }}
                                                >
                                                    {row.tech}
                                                </Typography>
                                                }
                                            sx={{
                                                display: 'flex',
                                                justifyContent: 'space-between',
                                            
                                            }}

                                        />
                                        
                                    
                                    </ListItemButton>
                                    <Button onClick={() => handleAddMetrics(row)} > 
                                        <AddIcon />
                                    </Button>
                                </Stack>
                            ))}
                        </List>
                  

                        <Button variant="h7" sx={{ width: '55%', ml:11 ,mt:4, mb:4,bgcolor: '#DEDEDE', boxShadow: '0px 2px 4px rgba(0, 0, 0, 0.1)' }}>
                            ADD / REQUEST METRIC
                        </Button>
                    
                    </Paper>
                </Grid>
                
                <Grid item xs={12} md={8} lg={6}>
                {Object.keys(selectedItem).length > 0 ? (
                       <GoalMetricsDetailBox
                       selectedItem={selectedItem}
                       userDataList={userDataList}
                       selectedItemStatus={selectedItemStatus}
                       />  
                    ):(
                        <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column', height: '100%', mr: 8, bgcolor: '#D9D9D9'}}>
                <Typography 
                    component="h1" 
                    variant="h6" 
                    sx={{ 
                        mt: 2, textAlign: 'center' 
                    }}>
                        Please select metrics to show details
                </Typography>
            </Paper>
                    )}
                </Grid>
                

               
            </Grid>
        </Box>
    );
}
</file>

<file path="src/FinancePageComponents/PlanningComponents/PlanningDetailBox.js">
import * as React from 'react';
import { useState, useEffect } from "react";
import ListItem from '@mui/material/ListItem';
import {Typography, Paper, List, LinearProgress, Box, Stack, ListItemText, Avatar, Button, 
    Dialog, DialogActions, DialogContent, DialogTitle, FormControl} from '@mui/material';
import FinancialMetricsTable from '../../OverviewPageComponents/FinancialMetricsTable';
import EditIcon from '@mui/icons-material/Edit';
import EditMetricBox from '../EditMetricBox';
import { DatePicker } from '@mui/x-date-pickers'
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import dayjs from 'dayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { getFirestore, doc, updateDoc, query, collection, getDocs, where, onSnapshot} from 'firebase/firestore'
import firebaseApp from '../../firebase-config';
import { set } from 'firebase/database';

// Connect to current firebase project
const firestore = getFirestore(firebaseApp);
const user_email = window.localStorage.getItem('user_email');

export default function PlanningDetailBox(props) {
    const row = props.row
    const userDataList = props.userDataList
    const [selectedItemDatasource, setSelectedItemDatasource] = useState([]);
    const [selectedItemSensorData, setSelectedItemSensorData] = useState([]);
    const [editDateOpen, setEditDateOpen] = useState(false);
    const [editMetricOpen, setEditMetricOpen] = useState(false);
    const [completionRate, setCompletionRate] = useState("0%");
    const [dueDate, setDueDate] = useState("");
    const [jsDueDate, setJsDueDate] = useState(dayjs()); 
    const [selectedMetric, setSelectedMetric] = useState("");
    const [metricDueDateList, setMetricDueDateList] = useState([]);
    const [location, setLocation] = useState("");

    useEffect(() => {
        console.log(row);
        let datasource = userDataList.filter((item) =>
            row.datasource.includes(item.name)
          )
        setSelectedItemDatasource(datasource);

        let sensorData = userDataList.filter((item) =>
            row.sensorFieldData.includes(item.name)
          )
        setSelectedItemSensorData(sensorData);
        
        const allDataSource = datasource.concat(sensorData)

        const onTrackDatasource = allDataSource.filter((item) =>
            item.status == "On Track"
          )

        let rate = (onTrackDatasource.length/allDataSource.length * 100).toFixed(0) + '%';
        setCompletionRate(rate)
        // setDueDate(getDueDate(allDataSource[0].createdAt,30))
       

    }, [row, userDataList])

    useEffect(() => {
        const userQuery = query(
            collection(firestore, 'users'),
            where('email', '==', user_email),
            );

            onSnapshot(userQuery, snapshot => {
                const user = snapshot.docs.map(doc =>  doc.data() )
                // setMetricDueDateList(user[0].metricDueDate)
                setLocation(user[0].location)
            })

    }, [])


    const handleEditMetricOpen = (metric) => {
        setSelectedMetric(metric)
        setEditMetricOpen(true)
        
    };
    const handleEditDateOpen = () => {
        setEditDateOpen(true)
    }
    const handleEditDateClose = () => {
        setEditDateOpen(false)
        setJsDueDate(dayjs(dueDate))
    }
   
    const getDueDate = (date,days) => {
        const milliseconds = date.seconds * 1000 + Math.round(date.nanoseconds / 1000000);
        const currentDate = new Date(milliseconds);
        const futureDate = new Date();
        futureDate.setDate(currentDate.getDate() + days);
        const futureDateDayjs = dayjs(futureDate);
        setJsDueDate(futureDateDayjs);
        const formattedDate = futureDateDayjs.format('MMMM DD, YYYY')
            return formattedDate;
    };


    const handleEditDateSubmit = () => {
        setDueDate(jsDueDate.format('MMMM DD, YYYY'))
        // const q = query(collection(firestore, 'users'), where("user_email", "==", user_email));
        setEditDateOpen(false)
    }
    
        

    return(
        <Paper elevation={3} sx={{  mt:-1, ml: 2, mb: 2, mr:2, minWidth: 420, maxWidth: 420 }}>
            <Typography 
                component="h1"
                variant="h6"
                
                fontWeight='bold'
                sx={{
                    mt: 2,
                    ml: 2,
                }}
            >
                {row.name}
            </Typography>
            <Typography 
                variant="subtitle1"
                sx={{
                    mt: 2,
                    ml: 2,
                }}
            >
                Completion Rate
            </Typography>
            {row.type === 'Operational' || row.type === 'Financial' ? (
                <Avatar
                    sx={{ width: 50, height: 50, alignSelf: 'center', ml: 4 }}
                >
                    {row.type === 'Operational' ? 'OP' : 'FI'}
                </Avatar>
            ) : null}
            <Stack direction="row" spacing={1} alignItems="center">
                <Box width="100%" sx={{ ml: 2 }}>
                    <LinearProgress variant="determinate" value={parseInt(completionRate, 10)} />
                </Box>
                <Box minWidth={35}>
                    <Typography variant="body2" color="textSecondary">
                    {completionRate}
                    </Typography>
                </Box>
            </Stack>
            <Typography 
                variant="subtitle1"
                sx={{
                    mt: 2,
                    ml: 2,
                }}
            >
                Benchmarks: From  {row.targetRangeLow} to {row.targetRangeHigh} {row.unit}
            </Typography>
            <Stack direction="row" spacing={0} alignItems="center" sx={{ mt: 1, mb: 2 }}>
            {/* {row.dueDate ? (
            <Typography 
                variant="subtitle1"
                sx={{
                    mt: 1,
                    ml: 2,
                }}
            >
                Due Date: {row.dueDate}
            </Typography>
            ):(
            <Typography 
                variant="subtitle1"
                sx={{
                    mt: 1,
                    ml: 2,
                }}
            >
                Due Date: {dueDate}
            </Typography>

            )}
              <Button onClick={() => handleEditDateOpen(row)} sx={{ mt: 2 }}>
                <EditIcon />
            </Button>
            <Dialog open={editDateOpen} onClose={handleEditDateClose} maxWidth={"sm"} fullWidth={true}>
            <DialogTitle>Edit Due Date</DialogTitle>
                <DialogContent>
                    
                        <FormControl sx={{ ml: 4, mt: 1 }}>
                        <LocalizationProvider dateAdapter={AdapterDayjs}>
                            <DatePicker
                                value={jsDueDate}
                                onChange={(date) => setJsDueDate(date)}
                            />
                        </LocalizationProvider>
                         </FormControl>      
                </DialogContent>
            
            <DialogActions>
                <Button onClick={handleEditDateClose}>Cancel</Button>
                <Button onClick={handleEditDateSubmit}>Submit</Button>
            </DialogActions>
        </Dialog> */}
            </Stack>
            <Typography 
                variant="subtitle1"
                sx={{
                    mt: 2,
                    ml: 2,
                }}
            >
                Data Source:
            </Typography>

            <List sx={{ ml: 1}}>
                {selectedItemDatasource.map((row) => (
                    <ListItem sx={{ mt: -2, mb: -1 }}
                        secondaryAction={
                            <ListItemText
                            primary={row.status}
                            sx={{
                                color: row.status == 'On Track' ? 'green' : 'red',
                                fontWeight: 'bold',
                            }}
                            />
                        }
                    >
                        <ListItemText
                            primary={row.name}
                        />
                    </ListItem>
            
                ))}
            </List>

            <Typography 
                variant="subtitle1"
                sx={{
                    mt: 2,
                    ml: 2,
                }}
            >
                Sensor Data:
            </Typography>

            <List sx={{ ml: 1}}>
            {selectedItemSensorData.length>0 ?(
                selectedItemSensorData.map((row) => (
                    <ListItem sx={{ mt: -2, mb: -1 }}
                        secondaryAction={
                            <ListItemText
                            primary={row.status}
                            sx={{
                                color: row.status == 'On Track' ? 'green' : 'red',
                                fontWeight: 'bold',
                            }}
                            />
                        }
                    >
                        <ListItemText
                            primary={row.name}  
                        />
                    </ListItem>
            
                ))):(
                    <Typography
                        component="h1"
                        variant="h7"
                        wrap
                        sx={{  ml: 3, mb: 1}}
                    >
                        Not Applicable
                    </Typography>
                )}
            </List>
            {row.metricValue ?( 
                row.type == "Operational" ? (
                <List sx={{ mr: 1 }}>
            <Stack direction="row" spacing={0} alignItems="center" sx={{ mt: 1, mb: 2 }}>
                <ListItem sx={{ mt: -2, mb: -1 }}
                secondaryAction={
                    <ListItemText
                    primary= {`${row.metricValue} ${row.unit}`}
                    />
                }
                >
                <ListItemText
                    primary= "Metrics Value:"
                />
                
            </ListItem>
            <Button onClick={() => handleEditMetricOpen(row)} sx={{ mt: -1 }}>
                <EditIcon />
            </Button>

            <EditMetricBox editMetricOpen={editMetricOpen} setEditMetricOpen={setEditMetricOpen} data= {selectedMetric} location={location} action= "Edit"/>

            </Stack>
            <ListItem sx={{ mt: -2, mb: -1 }}
                secondaryAction={
                    <ListItemText
                    primary={(new Date(row.timestamp)).toLocaleDateString("en-US", {
                        day: "numeric",
                        month: "long",
                        year: "numeric"
                    })}
                    />
                }
                >
                <ListItemText
                    primary= "Time Stamp:"
                />
            </ListItem>
            </List>
                ):
                row.type == "Financial" && (
                    <>
                        <ListItem sx={{ mb: -1 }}
                            secondaryAction={
                                <Button onClick={() => handleEditMetricOpen(row)} sx={{ mt: 1 }}>
                                <EditIcon />
                            </Button>

                            }
                        >
                            <ListItemText
                                primary= "Metrics Value:"
                            />
                            
                        </ListItem>
                        <EditMetricBox editMetricOpen={editMetricOpen} setEditMetricOpen={setEditMetricOpen} data= {selectedMetric} location={location} action="Edit"/>

                        <FinancialMetricsTable metricValue= {row.metricValue} metricUnit= {row.metricUnit} metricName="" paperwide = {400} paperHeight = {250}/>

                    </>
                )):(
                    row.type == "Operational" ? (
                        <List sx={{ mr: 1 }}>
                    <Stack direction="row" spacing={0} alignItems="center" sx={{ mt: 1, mb: 2 }}>
                        <ListItem sx={{ mt: -2, mb: -1 }}
                        secondaryAction={
                            <ListItemText
                            primary= "Add Metrics:"
                            />
                        }
                        >
                        <ListItemText
                            primary= "No metrics value yet."
                        />
                        
                    </ListItem>
                    <Button onClick={() => handleEditMetricOpen(row)} sx={{ mt: -1 }}>
                        <EditIcon />
                    </Button>
        
                    <EditMetricBox editMetricOpen={editMetricOpen} setEditMetricOpen={setEditMetricOpen} data= {selectedMetric} location={location} action="Add"/>
        
                    </Stack>

                    </List>
                        ):
                        row.type == "Financial" && (
                            <Stack direction="row" spacing={0} alignItems="center" sx={{ mt: 1, mb: 2 }}>
                            <ListItem sx={{ mt: -2, mb: -1 }}
                            secondaryAction={
                                <ListItemText
                                primary= "Add Metrics:"
                                />
                            }
                            >
                            <ListItemText
                                primary= "No metrics value yet."
                            />
                            
                        </ListItem>
                        <Button onClick={() => handleEditMetricOpen(row)} sx={{ mt: -1 }}>
                            <EditIcon />
                        </Button>
            
                        <EditMetricBox editMetricOpen={editMetricOpen} setEditMetricOpen={setEditMetricOpen} data= {selectedMetric} location={location} action="Add"/>
            
                        </Stack>
    
                        )
                )}
                 
        </Paper>
    )
}
</file>

<file path="src/FinancePageComponents/PlanningPage.js">
import * as React from 'react';
import { useState, useEffect } from "react";
import ListItem from '@mui/material/ListItem';
import {Typography, Paper, List, Box, } from '@mui/material';
import { getFirestore, collection, onSnapshot, query, limit, orderBy, where } from 'firebase/firestore'
import firebaseApp  from "../firebase-config"
import PlanningDetailBox from './PlanningComponents/PlanningDetailBox';

// Connect to current firebase project
const firestore = getFirestore(firebaseApp);


export default function PlanningPage() {
    const industry = window.localStorage.getItem('industry');
    const user_email = window.localStorage.getItem('user_email');
    const [userSelectedMetricIds, setUserSelectedMetricIds] = useState([]);
    const [selectedMetrics, setSelectedMetrics] = useState([]);
    const [selectedMetricList, setSelectedMetricList] = useState([]);
    const [userDataList, setUserDataList] = useState([]);

    // Get user Selected Metrics ID List
    useEffect(() => {
        const userQuery = query(
          collection(firestore, 'users'),
          where('email', '==', user_email)
        );
          const unsubscribe = onSnapshot(userQuery, snapshot => {
            const user = snapshot.docs.map(doc => doc.data());
            setUserSelectedMetricIds(user[0].selectedMetricIds);
          })
  
          return () => {
            unsubscribe()
          }
        }, [])

        // Get esisting user data list of the user from [Third party](() => {
        const userDataQuery = query(
            collection(firestore, 'userData'),
            where('user_email', '==', user_email)
        );
    
        const unsubscribe = onSnapshot(userDataQuery, snapshot => {
             const userData = snapshot.docs.map(doc => doc.data());
             setUserDataList(userData);
            })

            return () => {
            unsubscribe()
            }
        }, [])

    // Get all metrics list and set the selected metric list base on user's Selected Metrics ID List
    useEffect(() => {
        const metricsQuery = query(
            collection(firestore, 'metrics'),
            where('industry', '==', industry),
            orderBy('id')
            );

        onSnapshot(metricsQuery, snapshot => {
            const metrics = snapshot.docs.map(doc => doc.data());
            const selectedMetrics = metrics.filter(metric => userSelectedMetricIds.includes(metric.id));
            setSelectedMetricList(selectedMetrics)

        })
    }, [userSelectedMetricIds]);


    // Query userMetrics
    useEffect(() => {
    const userMetricsQuery = query(
        collection(firestore, 'userMetrics'),
        where('user_email', '==', user_email),
        where('industry', '==', industry),
    );

    const unsubscribe = onSnapshot(userMetricsQuery, snapshot => {
        const data = snapshot.docs.map((doc) => doc.data());

        // Map the metrics value from userMetrics collection to the selectedMetrics
        const updatedPlanningMetrics = selectedMetricList.map((item) => {
            const matchingDataItem = data.find((dataItem) => item.name === dataItem.metricsName);
            if (matchingDataItem) {
                
              return {
                ...item,
                Recommendation: "",
                CompletionRate: "0%",
                metricValue: matchingDataItem.value,
                metricUnit: matchingDataItem.unit,
                metricsId: item.id,
                userMetricsId: matchingDataItem.id,
                timestamp: matchingDataItem.dataEdit.toDate(),
                type: matchingDataItem.type
              };
            }
            else{
                return {
                    ...item,
                    Recommendation: "",
                    CompletionRate: "0%",
                    metricsId: item.id,
                  };
            }
            
          });

          // Store the update metrics list that contain metric value selectedMetrics
          setSelectedMetrics(updatedPlanningMetrics);  
          console.log(updatedPlanningMetrics)
    })
    return () => {
        unsubscribe()
      }
    }, [selectedMetricList])


    const getDueDate = (date,days) => {
    const futureDate = new Date();
    futureDate.setDate(date + days);
    const formattedDate = futureDate.toLocaleDateString("en-US", {
        day: "numeric",
        month: "long",
        year: "numeric"
        });
        return formattedDate;
};

    // Display every selected metric in Planning page
    return (
        
            
        <Box sx={{ flexGrow: 1, width: '100%', height:'80%', bgcolor: '#D9D9D9'}}>
            <ListItem>
                <Typography
                    component="h1"
                    variant="h6"
                    color="inherit"
                    noWrap
                    sx={{ flexGrow: 1,fontWeight: 'bold', mt:2, ml:2, mr: 3 }}
                >
                    Plans
                </Typography>

            </ListItem>
            {selectedMetrics.length > 0 ? (
            <Box sx={{  overflowX: 'auto' }}>
                <List sx={{ display: 'flex' }}>
                {selectedMetrics?.map((row) => (
                <PlanningDetailBox row={row} userDataList={userDataList} />
               ))}
            </List>
            </Box>)
            : (
            <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column', height: '100%', mr: 8, bgcolor: '#D9D9D9'}}>
                <Typography 
                    component="h1" 
                    variant="h6" 
                    sx={{ 
                        mt: 2, textAlign: 'center' 
                    }}>
                        Please select metrics in Goal Metrics Page.
                </Typography>
            </Paper>
        )}
        </Box>
    );
}
</file>

<file path="src/firebase-config.js">
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseApp = initializeApp({
  apiKey: "[redacted]",
  authDomain: "[redacted-project].firebaseapp.com",
  databaseURL: "https://[redacted-project]-default-rtdb.firebaseio.com",
  projectId: "[redacted-project]",
  storageBucket: "[redacted-project].appspot.com",
  messagingSenderId: "623647192124",
  appId: "1:623647192124:web:1a2ebb2d8b8eedfacc3f39",
  measurementId: "G-ZN23WW1HXV"
});

export default firebaseApp;
</file>

<file path="src/index.js">
import React from 'react';
import ReactDOM from 'react-dom/client';
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import Dashboard from './Dashboard';
import SignUpPage from './SignUpPage';
import SignInPage from './SignInPage';
import OnboardPage from './OnboardPage';
import SummaryPage from './SummaryPage';
import OverviewPage from './OverviewPage';
import ProfilePage from './ProfilePage';
import SettingsPage from './ProfileSettingPage';
import FinancePage from './FinancePage';
import ServiceRequestPage from './ServiceRequestPage';
import DataLibraryPage from './DataLibraryPage';
import AddDataPage from './DataPageComponents/AddDataPage';
import ManualInputPage from './DataPageComponents/ManualInputPage';
import ImportDataPage from './DataPageComponents/ImportDataPage';
import SyncDataPage from './DataPageComponents/SyncDataPage';


const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <React.StrictMode>
    <Router>
            <Routes>
              <Route path='/' element={<SignInPage />} />
              <Route path='/SignUp' element={<SignUpPage />} />
              <Route path='/Onboard' element={<OnboardPage />} />
              <Route path='Dashboard' element={<Dashboard />} >
                <Route  path='Welcome' element={<SummaryPage />} />
                <Route  path='Overview' element={<OverviewPage />} />    
                <Route path="Finance/Planning" element={<FinancePage selectedTab={0} />} />
                <Route path="Finance/GoalMetrics" element={<FinancePage selectedTab={1} />} />
                <Route path="Finance/DataSelection" element={<FinancePage selectedTab={2} />} />
                <Route path="Finance/ActionPlans" element={<FinancePage selectedTab={3} />} />

                <Route  path='ServiceRequest' element={<ServiceRequestPage />} />  
                <Route  path='Data/DataLibrary' element={<DataLibraryPage/>} />
                <Route  path='Data/DataLibrary/AddData' element={<AddDataPage/>} />
                <Route  path='Data/DataLibrary/AddData/ManualInput' element={<ManualInputPage/>} />
                <Route  path='Data/DataLibrary/AddData/ImportData' element={<ImportDataPage/>} />
                <Route  path='Data/DataLibrary/AddData/SyncData' element={<SyncDataPage/>} />
                <Route  path='Profile' element={<ProfilePage />} />
                  <Route  path='/Dashboard/Profile/Settings' element={<SettingsPage />} />
              </ Route>
            </Routes>
          </Router>      
  </React.StrictMode>
);
</file>

<file path="src/OnboardPage.js">
import Logo from './pics/Logo_White-03.svg'; 
import * as React from 'react';
import { createTheme, ThemeProvider} from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Select from '@mui/material/Select';
import FormControl from "@mui/material/FormControl";
import Button from '@mui/material/Button';
import LinearProgress from '@mui/material/LinearProgress';
import { Paper, Box, RadioGroup, FormControlLabel, Radio, Grid, InputAdornment, } from '@mui/material';
import { useNavigate } from "react-router-dom";
import { useState } from "react";
import { getFirestore, doc, setDoc } from 'firebase/firestore'
import { getAuth } from "firebase/auth";
import firebaseApp from './firebase-config';

// Connect to current firebase project
const firestore = getFirestore(firebaseApp);

/* Identify the current user */
const user_email = window.localStorage.getItem('user_email');
const uid = window.localStorage.getItem('uid');

const mdTheme = createTheme({
    palette: {
      mode: 'dark',
      background: {
        default: '#031c4a',
        paper: '#031c4a',
      },
      error: {
        main: '#060c43',
      },
      warning: {
        main: '#00e676',
      },
      success: {
        main: '#ffb74d',
      },
    },
  });

const auth = getAuth();

export default function OnboardPage() {
    const navigate = useNavigate();
    if(!user_email) navigate("/");

    const [show1, setShow1] = useState(true)
    const [show2, setShow2] = useState(false)
    const [show3, setShow3] = useState(false)

    const [firstName, setFirstName] = useState("")
    const [lastName, setLastName] = useState("")
    const [location, setLocation] = useState("")
    const [subscriptionPlan, setSubscriptionPlan] = useState("")
    const [phoneNumber, setPhoneNumber] = useState("")
    const [goal, setGoal] = useState("")
    const [role, setRole] = useState("")
    const industryRecord = window.localStorage.getItem('industry');
    const [industry, setIndustry] = useState(window.localStorage.getItem('industry'))
   

    /* Handle personal data uploading */
    const onSubmit = () => {
        if (industryRecord){
            setIndustry(industryRecord)
        }
        if (firstName == "" || lastName == "" || location == "" || phoneNumber == "" || goal == "" || role == "" || industry == "" || subscriptionPlan == "") {
            alert("Please complete all the question!")
        } else {
            let isUpgrade = false;
            if (subscriptionPlan == "Pro") {
                isUpgrade = true;
            }
            const userCredentials = {
                firstName: firstName,
                lastName: lastName,
                username: user_email,
                phoneNumber: phoneNumber,
                location: location,
                email: user_email,
                createdAt: new Date().toISOString(),
                userId: uid,
                goal: goal,
                industry: industry,
                role: role,
                isUpgrade: isUpgrade,
                subscriptionPlan: subscriptionPlan,
            }
            const userRef = doc(firestore, 'users/'+user_email)
            setDoc(userRef, userCredentials)
            alert("Completed! Thank you, now let's start!")
            navigate('/Dashboard/Welcome')
        }
    }

    const next1 = () => {
        setShow1(false)
        setShow2(true)
    }

    const next2 = () => {
        setShow2(false)
        setShow3(true)
    }

    const previous1 = () => {
        setShow1(true)
        setShow2(false)
    }
    
    const previous2 = () => {
        setShow2(true)
        setShow3(false)
    }

    return (
        <ThemeProvider theme={mdTheme}>
            <Box sx={{ display: 'flex' }}>
            <CssBaseline />
                <Box sx={{ height: "100vh", width: "100%", pt: 5, pl: 8 }}>
                    {/* Welcome title */}
                    {show1 && 
                        <Paper sx={{ display: 'flex', minWidth: 700, minHeight: 680 }}>
                            <Box>
                                <Box sx={{ minHeight: 60 }} />
                                <Box sx={{ maxWidth: 100, ml: '47%', mb: 3 }}>
                                    <LinearProgress variant="determinate" value={33} />
                                </Box>
                                <Box display="flex" justifyContent="center" alignItems="center">
                                    <Typography
                                        component="h1"
                                        variant="h6"
                                        noWrap
                                        sx={{ ml: 8, mt: 3 }}
                                        style={{ fontWeight: 600 }}
                                    >
                                        Welcome to Ambientsystems!
                                    </Typography>
                                </Box>
                                <Box display="flex" justifyContent="center" alignItems="center">
                                    <Typography
                                        component="h1"
                                        variant="h7"
                                        noWrap
                                        color="#708090"
                                        sx={{ ml: 8, mt: 2 }}
                                    >
                                        Help us customize your experience by telling 
                                    </Typography>
                                </Box>
                                <Box display="flex" justifyContent="center" alignItems="center">
                                    <Typography
                                        component="h1"
                                        variant="h7"
                                        noWrap
                                        color="#708090"
                                        sx={{ ml: 8 }}
                                    >
                                        us a bit about yourself and your goal.
                                    </Typography>
                                </Box>

                                {/* Profile data */}
                                <Typography
                                    component="h1"
                                    variant="h7"
                                    noWrap
                                    sx={{ ml: "20%", mt: 4 }}
                                >
                                    Let's know you better:
                                </Typography>

                                <FormControl sx={{ ml: "25%", mt: 1 }}>
                                    <Box sx={{ mt: 3 }}>
                                        <TextField id="firstName" label="First Name" variant="standard" onChange={(e) => setFirstName(e.target.value)}/>
                                        <TextField id="lastName" label="Last Name" variant="standard" sx={{ ml: 5 }} onChange={(e) => setLastName(e.target.value)}/>
                                    </Box>

                                    <Box sx={{ mt: 3 }}>
                                    <Select native defaultValue="" id="location" label="Select Location"  
                                        onChange={(e) => {setLocation(e.target.value)}}
                                    >
                                        <option aria-label="" value="">Location</option>
                                        <option value="Canada">Canada</option>
                                        <option value="Singapore">Singapore</option>
                                        <option value="Hong Kong (China)">Hong Kong (China)</option>
                                        
                                    </Select>
                                        <TextField id="phoneNumber" label="Phone Number" variant="standard" sx={{ ml: 5 }} onChange={(e) => setPhoneNumber(e.target.value)}/>
                                    </Box>

                                  <Box sx={{ mt: 5 }}>
                                        <TextField id="email" label="Email Address" variant="standard" defaultValue={user_email}
                                            InputProps={{
                                                readOnly: true,
                                        }}/>
                                    </Box>
                                </FormControl>

                                <Typography
                                    component="h1"
                                    variant="h7"
                                    noWrap
                                    sx={{ ml: "20%", mt: 5 }}
                                >
                                    Choose your subscription plan:
                                </Typography>

                                <FormControl sx={{ ml: "20%", mt: 1 }}>
                                    <Box display="flex" sx={{ mt: 3 }}>
                                        <RadioGroup
                                            aria-labelledby="goal-radio-buttons-group-label"
                                            defaultValue=""
                                            name="goal-radio-buttons-group"
                                            onChange={(e) => setSubscriptionPlan(e.target.value)}
                                        >
                                            <Grid container spacing={10}>
                                                <Grid item xs={6}>
                                                    <FormControlLabel value="Basic" control={<Radio />} label="Basic" />
                                                </Grid>
                                                <Grid item xs={6}>
                                                    <FormControlLabel value="Pro" control={<Radio />} label="Pro" />
                                                </Grid>
                                            </Grid>
                                        </RadioGroup>
                                    </Box>
                                </FormControl>

                                <Box sx={{ mt: 3, ml: 8, display: "flex" }}>
                                    <Button variant="contained" color='primary' component="label" sx={{ mt: 2, ml: 74 }} onClick={next1}>
                                        next
                                    </Button>
                                </Box>
                            </Box>
                        </Paper>
                    }
                    {show2 &&
                        <Paper sx={{ display: 'flex', minWidth: 700, minHeight: 680 }}>
                            <Box>
                                <Box sx={{ minHeight: 60 }} />
                                <Box sx={{ maxWidth: 100, ml: '47%', mb: 3 }}>
                                    <LinearProgress variant="determinate" value={66} />
                                </Box>
                                <Box display="flex" justifyContent="center" alignItems="center">
                                    <Typography
                                        component="h1"
                                        variant="h6"
                                        noWrap
                                        sx={{ ml: 8, mt: 3 }}
                                        style={{ fontWeight: 600 }}
                                    >
                                        Almost there..
                                    </Typography>
                                </Box>
                                <Box display="flex" justifyContent="center" alignItems="center">
                                    <Typography
                                        component="h1"
                                        variant="h7"
                                        noWrap
                                        color="#708090"
                                        sx={{ ml: 8, mt: 2 }}
                                    >
                                        Help us customize your experience by telling 
                                    </Typography>
                                </Box>
                                <Box display="flex" justifyContent="center" alignItems="center">
                                    <Typography
                                        component="h1"
                                        variant="h7"
                                        noWrap
                                        color="#708090"
                                        sx={{ ml: 8 }}
                                    >
                                        us a bit about yourself and your goal.
                                    </Typography>
                                </Box>

                                {/* Goal data */}
                                <Typography
                                    component="h1"
                                    variant="h7"
                                    noWrap
                                    sx={{ ml: "20%", mt: 4 }}
                                >
                                    What is your main goal?
                                </Typography>

                                <FormControl sx={{ ml: "20%", mt: 1 }}>
                                    <Box display="flex" sx={{ mt: 3 }}>
                                        <RadioGroup
                                            aria-labelledby="goal-radio-buttons-group-label1"
                                            defaultValue=""
                                            name="goal-radio-buttons-group1"
                                            onChange={(e) => setGoal(e.target.value)}
                                        >
                                            <Grid container>
                                                <Grid item xs={6}>
                                                    <FormControlLabel value="Achieve regulatory requirements" control={<Radio />} label="Achieve regulatory requirements" />
                                                    <FormControlLabel value="Identify new decarbonization technologies" control={<Radio />} label="Identify new decarbonization technologies" />
                                                    <FormControlLabel value="Find a consultancy" control={<Radio />} label="Find a consultancy" />
                                                </Grid>
                                                <Grid item xs={6}>
                                                    <FormControlLabel value="Evaluate scenarios" control={<Radio />} label="Evaluate scenarios" />
                                                    <FormControlLabel value="Minimize my emissions" control={<Radio />} label="Minimize my emissions" />
                                                    <FormControlLabel value="Achieve lower energy-intensity of my services" control={<Radio />} label="Achieve lower energy-intensity of my services" />
                                                </Grid>
                                            </Grid>
                                        </RadioGroup>
                                    </Box>
                                </FormControl>
                                {!industryRecord && (
                                <>
                                <Typography
                                    component="h1"
                                    variant="h7"
                                    noWrap
                                    sx={{ ml: "20%", mt: 4 }}
                                >
                                    What is your industry?
                                </Typography>

                                <FormControl sx={{ ml: "20%", mt: 1 }}>
                                    <Box display="flex" sx={{ mt: 3 }}>
                                        <RadioGroup
                                            aria-labelledby="goal-radio-buttons-group-label"
                                            defaultValue=""
                                            name="goal-radio-buttons-group"
                                            onChange={(e) => setIndustry(e.target.value)}
                                        >
                                            <Grid container spacing={10}>
                                                <Grid item xs={6}>
                                                    <FormControlLabel value="Transportation" control={<Radio />} label="Transportation" />
                                                    <FormControlLabel value="Real Estate" control={<Radio />} label="Real Estate" />
                                                </Grid>
                                                <Grid item xs={6}>
                                                    <FormControlLabel value="Vertical Farming" control={<Radio />} label="Vertical Farming" />
                                                </Grid>
                                            </Grid>
                                        </RadioGroup>
                                    </Box>
                                </FormControl>
                                </>
                                )}

                                <Box sx={{ mt: 12, ml: 8, display: "flex" }}>
                                    <Button variant="contained" color='primary' component="label" sx={{ mt: 2, ml: 58 }} onClick={previous1}>
                                        previous
                                    </Button>
                                    <Button variant="contained" color='primary' component="label" sx={{ mt: 2, ml: 3 }} onClick={next2}>
                                        next
                                    </Button>
                                </Box>
                            </Box>
                        </Paper>
                    }
                    {show3 &&
                        <Paper sx={{ display: 'flex', minWidth: 700, minHeight: 680 }}>
                            <Box>
                                <Box sx={{ minHeight: 60 }} />
                                <Box sx={{ maxWidth: 100, ml: '47%', mb: 3 }}>
                                    <LinearProgress variant="determinate" value={99} />
                                </Box>
                                <Box display="flex" justifyContent="center" alignItems="center">
                                    <Typography
                                        component="h1"
                                        variant="h6"
                                        noWrap
                                        sx={{ ml: 8, mt: 3 }}
                                        style={{ fontWeight: 600 }}
                                    >
                                        Let's get started!
                                    </Typography>
                                </Box>
                                <Box display="flex" justifyContent="center" alignItems="center">
                                    <Typography
                                        component="h1"
                                        variant="h7"
                                        noWrap
                                        color="#708090"
                                        sx={{ ml: 8, mt: 2 }}
                                    >
                                        Help us customize your experience by telling 
                                    </Typography>
                                </Box>
                                <Box display="flex" justifyContent="center" alignItems="center">
                                    <Typography
                                        component="h1"
                                        variant="h7"
                                        noWrap
                                        color="#708090"
                                        sx={{ ml: 8 }}
                                    >
                                        us a bit about yourself and your goal.
                                    </Typography>
                                </Box>

                                {/* Goal data */}
                                <Typography
                                    component="h1"
                                    variant="h7"
                                    noWrap
                                    sx={{ ml: "20%", mt: 4 }}
                                >
                                    What is your role?
                                </Typography>

                                <FormControl sx={{ ml: "47%", mt: 1 }}>
                                        <RadioGroup
                                            aria-labelledby="roal-radio-buttons-group-label"
                                            defaultValue=""
                                            name="roal-radio-buttons-group"
                                            onChange={(e) => setRole(e.target.value)}
                                        >
                                            <FormControlLabel value="Finance" control={<Radio />} label="Finance" />
                                            <FormControlLabel value="Marketing" control={<Radio />} label="Marketing" />
                                            <FormControlLabel value="Operations" control={<Radio />} label="Operations" />
                                            <FormControlLabel value="Development" control={<Radio />} label="Development" />
                                        </RadioGroup>
                                </FormControl>

                                <Box sx={{ mt: 11, ml: 8, display: "flex" }}>
                                    <Button variant="contained" color='primary' component="label" sx={{ mt: 2, ml: 58 }} onClick={previous2}>
                                        previous
                                    </Button>
                                    <Button variant="contained" color='primary' component="label" sx={{ mt: 2, ml: 3 }} onClick={onSubmit}>
                                        submit
                                    </Button>
                                </Box>
                            </Box>
                        </Paper>
                    }
                </Box>

                <Box sx={{ height: "100vh", width: "75%", pt: 5 }}>
                    <img id="backgroundImg" src={Logo} alt="Logo" style={{ opacity: 0.2 }} />
                </Box>
            </Box>
        </ThemeProvider>
    );
}
</file>

<file path="src/OverviewPage.js">
import * as React from 'react';
import { useTheme } from '@mui/material/styles';
import DataStatusTable from './OverviewPageComponents/DataStatusTable';
import RecommendationTable from './OverviewPageComponents/RecommendationTable';
import CheckCircleOutlineIcon from '@mui/icons-material/CheckCircleOutline';
import MoreHorizIcon from '@mui/icons-material/MoreHoriz';
import { CalendarPicker, DATE_RANGE } from "mui-calendar-picker";
import {Typography,  Paper, Grid, Select, MenuItem, FormControl,FormControlLabel, 
    InputLabel, Stack, Checkbox, Container, InputAdornment, Avatar, Button, Box, List} from '@mui/material';
import { useState, useEffect } from "react";
import { getFirestore, collection, onSnapshot, query, where, orderBy } from 'firebase/firestore'
import OperationalMetricsTable from './OverviewPageComponents/OperationalMetricsTable';
import FinancialMetricsTable from './OverviewPageComponents/FinancialMetricsTable';
import firebaseApp from './firebase-config';

// Connect to current firebase project
const firestore = getFirestore(firebaseApp);

// Data for linechart in the middle of the page
function createData(time, amount) {
    return { time, amount};
}

/* Identify the current user */
const user_email = window.localStorage.getItem('user_email');

// Main function of this page
export default function OverviewPage() {
    const theme = useTheme();
    const [dateRange, setDateRange] = useState(DATE_RANGE);
    const [sites, setSites] = useState([]);
    const [score, setScore] = useState(0);
    const [chart, setChart] = useState([]);
    const [metric, setMetric] = useState("");
    const [metricId, setMetricId] = useState(0);
    const [metricsList, setMetricsList] = useState([]);
    const industry = window.localStorage.getItem('industry');
    const [financialMetricsList, setFinancialMetricsList] = useState([]);
    const [userSelectedMetricIds, setUserSelectedMetricIds] = useState([]);
    const [selectedMetricList, setSelectedMetricList] = useState([]);
    const [operationalMetricsList, setOperationalMetricsList] = useState([])
    const [cameraFeedOnTrack, setCameraFeedOnTrack] = useState(false);
    const [financailFeedOnTrack, setFinancialOnTrack] = useState(false);
    const [filter1, setFilter1] = useState([])
    const [filter2, setFilter2] = useState([])
    const [filter3, setFilter3] = useState([])
    const [selectedLocation, setSelectedLocation] = useState('All');
    const [user, setUser] = useState({})

    /* Firestore SDK queries */
    useEffect(() => {
        const metricsQuery = query(
            collection(firestore, 'metrics'),
            where('industry', '==', industry),
            orderBy('id')
            );

        onSnapshot(metricsQuery, snapshot => {
            const metrics = snapshot.docs.map(doc => ({id: doc.id, data: doc.data() }))
            setMetricsList(metrics)
        })
        
    }, []);
        // Get user Selected Metrics ID List
    useEffect(() => {
        const userQuery = query(
            collection(firestore, 'users'),
            where('email', '==', user_email)
        );
            const unsubscribe = onSnapshot(userQuery, snapshot => {
            const user = snapshot.docs.map(doc => doc.data());
            setUserSelectedMetricIds(user[0].selectedMetricIds);
            })
    
            return () => {
            unsubscribe()
            }
        }, [])
    
    // Get all metrics list and set the selected metric list base on user's Selected Metrics ID List
    useEffect(() => {
        const metricsQuery = query(
            collection(firestore, 'metrics'),
            where('industry', '==', industry),
            orderBy('id')
            );

        onSnapshot(metricsQuery, snapshot => {
            const metrics = snapshot.docs.map(doc => doc.data());
            const selectedMetrics = metrics.filter(metric => userSelectedMetricIds.includes(metric.id));
            setSelectedMetricList(selectedMetrics)
            console.log(selectedMetrics)
        })
    }, [userSelectedMetricIds]);

    // Query userMetrics
    useEffect(() => {
        const userMetricsQuery = query(
            collection(firestore, 'userMetrics'),
            where('user_email', '==', user_email),
            where('industry', '==', industry),
        );
    
        const unsubscribe = onSnapshot(userMetricsQuery, snapshot => {
            const data = snapshot.docs.map((doc) => doc.data());
    
            // Map the metrics value from userMetrics collection to the selectedMetrics
            const metricDetails = selectedMetricList.map((item) => {
                const matchingDataItem = data.find((dataItem) => item.name === dataItem.metricsName);
                if (matchingDataItem) {
                    
                    return {
                    ...item,
                    metricValue: matchingDataItem.value,
                    metricUnit: matchingDataItem.unit,
                    metricId: matchingDataItem.id,
                    };
                }
                else{
                    return item
                }
                });

                let operationalMetrics = [];
                let financialMetrics = [];
                    if (metricId == 0){
                        operationalMetrics = metricDetails.filter((item) => {
                        return item.type === "Operational" && item.metricValue;
                    });
                        financialMetrics = metricDetails.filter((item) => {
                        return item.type === "Financial" && item.metricValue;
                    })
                }
                else{
                    operationalMetrics = metricDetails.filter((item) => {
                        return item.id === metricId && item.type === "Operational" && item.metricValue;
                    });
                    financialMetrics = metricDetails.filter((item) => {
                        return item.id === metricId && item.type === "Financial" && item.metricValue;
                    })
                }
                setOperationalMetricsList(operationalMetrics)
                setFinancialMetricsList(financialMetrics);
                console.log(operationalMetrics)
        })
        return () => {
            unsubscribe()
            }
        }, [selectedMetricList, metricId])
        

    /* Return data for the linechart */
    function getDatesInRange(startDate, endDate) {
        const date = new Date(startDate.getTime());
      
        const dates = [];
        var count = 1;
      
        while ((date <= endDate) && (count <= 7)) {
          dates.push(new Date(date));
          date.setDate(date.getDate() + 1);
          count += 1;
        }

        return dates;
    }

    useEffect(() => {
        const res = getDatesInRange(new Date(dateRange.start), new Date(dateRange.end))
        var chartData = []

        for (let i = 0; i < res.length; i++) {
            var valueData = Math.floor(Math.random() * (100 - 1)) + 1
            chartData.push(createData(res[i].toDateString(), valueData))
        }
        console.log(chartData)
        setChart(chartData)

        const base = Math.floor(Math.random() * 6) - 3
        setScore(score + chartData.length * base)

    }, [dateRange])


    /* Calculate the carbon score */
    useEffect(() => {
        const connectorQuery = query(
            collection(firestore, 'connectors'),
            where('user_email', '==', user_email)
        );
        const unsubscribe = onSnapshot(connectorQuery, snapshot => {
            if (snapshot.docs.length > 0) {
                const randomNum = Math.floor(Math.random() * 5) + 2
                const res = 50 + randomNum * snapshot.docs.length

                if (res > 100) {
                    setScore(100)
                } else {
                    setScore(res)
                }
            } else {
                setScore(0)
            }
        })

        return () => {
            unsubscribe()
        }
        }, [])

    useEffect(() => {
        const userQuery = query(
            collection(firestore, 'users'),
            where('email', '==', user_email)
        );
            const unsubscribe = onSnapshot(userQuery, snapshot => {
            const user = snapshot.docs.map(doc => doc.data());
            setUser(user[0]);
            })
    
            return () => {
            unsubscribe()
            }
        }, [])

    useEffect(() => {
        if (filter1 == '') {
            setScore(score -  Math.floor(Math.random() * 4))
        } else {
            setScore(score +  Math.floor(Math.random() * 3))
        }
    }, [filter1])
    useEffect(() => {
        if (filter2 == '') {
            setScore(score -  Math.floor(Math.random() * 4))
        } else {
            setScore(score +  Math.floor(Math.random() * 3))
        }
    }, [filter2])
    useEffect(() => {
        if (filter3 == '') {
            setScore(score -  Math.floor(Math.random() * 4))
        } else {
            setScore(score +  Math.floor(Math.random() * 3))
        }
    }, [filter3])

    const handleMetricChange = (e) => {
        setMetric(e.target.value)
    };

    return (   
        <div> 
        {/* Title */}
        <Typography
            component="h1"
            variant="h5"
            color="inherit"
            noWrap
            sx={{ flexGrow: 1, mt:-3, ml: 6, mb: 2, fontWeight: 'bold' }}
        >
            Overview
        </Typography>

        <FormControl sx={{ ml: 6, minWidth: 150 }} variant= "standard">
            <Select native defaultValue="" id="grouped-native-select" label="Select Location" disableUnderline startAdornment={
                <InputAdornment position="start">
                    Location:
                </InputAdornment>
                }
                theme={theme}
                sx={{
                    backgroundColor: theme.palette.background.default,
                    padding: "0px 4px",
                }}
                onChange={(e) => {setSelectedLocation(e.target.value)}}
            >
                
                <option aria-label={user.location} value={user.location}>{user.location}</option>
                {/* <option aria-label="All" value="All">LOCATION</option>
                
                <option value="Canada">Canada</option>
                <option value="Singapore">Singapore</option>
                <option value="Hong Kong (China)">Hong Kong (China)</option> */}
            </Select>
        </FormControl>


        <Container maxWidth="lg" sx={{ mt: 2, ml:3, mr:5, mb: 4 }}>
            <Grid container spacing={3}>

                {/* First area to show camera feed */}
                <Grid item xs={12} md={8} lg={12}>
                    <Paper
                    sx={{
                        p: 2,
                        display: 'flex',
                        flexDirection: 'column',
                        height: 350,
                    }}
                    >
                        <Grid container spacing={3}>
                            {/* Camera Feed area */}
                            <Grid item xs={12} md={8} lg={3}>
                            <Stack direction="row" spacing={0}>
                                        <Typography
                                            component="h1"
                                            variant="h7"
                                            color="inherit"
                                            noWrap
                                            sx={{ flexGrow: 1, mt: 0.5, ml: 4, mb: -8, fontWeight: 'bold' }}
                                        >
                                            Camera Feed
                                        </Typography>
                                       
                                        <Stack direction="row" alignItems="center">
                                        <CheckCircleOutlineIcon 
                                            fontSize="small"  
                                            sx={{ 
                                                flexGrow: 1, 
                                                mt:0.5, 
                                                ml: 1, 
                                                color: cameraFeedOnTrack ? 'green' : 'inherit',
                                                }}/>
                                        <Typography
                                            component="h1"
                                            variant="h7"
                                            color="inherit"
                                            noWrap
                                            sx={{ 
                                                flexGrow: 1, 
                                                mt:0.5, 
                                                ml: 1, 
                                                color: cameraFeedOnTrack ? 'green' : 'inherit',
                                                }}
                                        >
                                            On Track
                                        </Typography>
                                        </Stack>
                                    </Stack>

                                    <Avatar
                                        alt="No Image Available"
                                        src="/src/pics/No_Image_Available.jpeg"
                                        sx={{ width: 170, height: 170, alignSelf: 'center', mt: 6, ml:6 }}
                                    />
                            </Grid>

                            {/* Linechart area */}

                            <Grid item xs={12} md={8} lg={9}>
                            <Stack direction="row" spacing={0} alignItems="center">
                            <Typography
                                component="h1"
                                variant="h7"
                                color="inherit"
                                noWrap
                                sx={{ flexGrow: 1, ml: 1, mb: 1, fontWeight: 'bold' }}
                            >
                                Financial Metrics
                            </Typography>
                            
                                 <Stack direction="row" alignItems="center">
                                        <CheckCircleOutlineIcon 
                                            fontSize="small"  
                                            sx={{ 
                                                flexGrow: 1, 
                                                mt:-1, 
                                                mr:1,
                                                color: financailFeedOnTrack ? 'green' : 'inherit',
                                                }}/>
                                        <Typography
                                            component="h1"
                                            variant="h7"
                                            color="inherit"
                                            noWrap
                                            sx={{ 
                                                flexGrow: 1, 
                                                mr:2,
                                                mt:-1, 
                                                color: financailFeedOnTrack ? 'green' : 'inherit',
                                                }}
                                        >
                                            On Track
                                        </Typography>
                                        </Stack>

                                    <Typography
                                        component="h1"
                                        variant="h7"
                                        color="inherit"
                                        noWrap
                                        sx={{
                                            flexGrow: 1,
                                            mt: -1,
                                            textAlign: 'center',
                                            backgroundColor: '#E0EDFB',
                                            padding: '1px 1px',
                                        }}
                                    >
                                        FINTECH
                                    </Typography>
                            
                                    <FormControl variant="standard" 
                                    sx={{ mt:-4, ml:2, mr:2, minWidth:200, maxWidth: 220, maxHeight:30 }}
                                    style={{ outline: 'none', boxShadow: 'none', border: 'none' }}
                                    >
                                        <InputLabel>Type of Metrics</InputLabel>
                                        <Select
                                        value={metric}
                                        onChange={handleMetricChange}
                                        label="Select Metrics"
                                        >
                                            <MenuItem value={0} onClick={() => setMetricId(0)}>
                                                All Metrics
                                            </MenuItem>
                                        {selectedMetricList.map((option) => ( 
                                            <MenuItem 
                                            key={option.name} 
                                            value={option.name}
                                            onClick={() => setMetricId(option.id)}
                                            >
                                            {option.name}
                                            </MenuItem>
                                        ))}
                                    </Select>
                                    </FormControl>
                        
                                    <CalendarPicker
                                    setDateRange={setDateRange}
                                    theme={theme}
                                    openBtnText={dateRange.start ? `${dateRange.start} - ${dateRange.end}` : "Select date range"}
                                    />
                                    <Button
                                        endIcon={<MoreHorizIcon />}
                                        sx={{
                                        flexGrow: 1,
                                        color: 'black',
                                        justifyContent: 'flex-end',
                                        maxWidth:20
                                        }}
                                        href="/Dashboard/Finance/Planning"
                                    >

                                    </Button>
                                </Stack>
                                {financialMetricsList.length > 0 ? (
                                <Box sx={{ overflowX: 'auto' }}>
                                    <List sx={{ display: 'flex' }}>
                                        {financialMetricsList?.map((row) => (
                                               
                                        <FinancialMetricsTable key={row.id} metricValue={row.metricValue} metricUnit={row.metricUnit} metricName={row.name} paperwide = {800} paperHeight = {250}/>
                                   
                                        ))}
                                    </List>
                                </Box>):(
                                    <Typography 
                                        component="h1" 
                                        variant="h6" 
                                        sx={{ 
                                            mt: 2, textAlign: 'center' 
                                        }}>
                                            No existing financial metrics.
                                    </Typography>)
                                }
                            </Grid>
                        </Grid>
                    </Paper>
                </Grid>

                {/* Data Status table */}
                <Grid item xs={12} md={8} lg={4}>
                    <Paper
                    sx={{
                        p: 0.5,
                        display: 'flex',
                        flexDirection: 'column',
                        height: 220,
                    }}
                    >
                        <DataStatusTable selectedLocation={selectedLocation}/>
                    </Paper>
                </Grid>

                {/* Operational Metrics Table */}
                <Grid item xs={12} md={8} lg={8}>
                    <Paper
                    sx={{
                        p: 0.5,
                        display: 'flex',
                        flexDirection: 'column',
                        height: 220,
                    }}
                    >
                        <OperationalMetricsTable dateRange={dateRange} operationalMetricsList={operationalMetricsList} />
                    </Paper>
                </Grid>
            </Grid>
            {/* Recommendations table */}
            <Grid item xs={12} mt={3} md={8} lg={4}>
                <Paper
                sx={{
                    p: 0.5,
                    display: 'flex',
                    flexDirection: 'column',
                    height: 220,
                }}
                >
                    <RecommendationTable metricId={metricId}/>
                </Paper>
            </Grid>
        </Container>
        </div> 
    );
}
</file>

<file path="src/OverviewPageComponents/dataStatusTable.js">
import * as React from 'react';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import { useState, useEffect } from "react";
import { getFirestore, collection, onSnapshot, query, where, } from 'firebase/firestore'
import MoreHorizIcon from '@mui/icons-material/MoreHoriz';
import firebaseApp from '../firebase-config';

// Connect to current firebase project
const firestore = getFirestore(firebaseApp);

/* Identify the current user */
const user_email = window.localStorage.getItem('user_email');

// Main function of this page
export default function DataStatusTable({selectedLocation}) {
  const [userDataList, setUserDataList] = useState([]);


  /* Firestore SDK queries */
    // Get esisting user data list of the user from [Third party](() => {
    const userDataQuery = query(
        collection(firestore, 'userData'),
        where('user_email', '==', user_email),
        where('selected', '==', true),
    );

    const unsubscribe = onSnapshot(userDataQuery, snapshot => {
          let userData = snapshot.docs.map(doc => doc.data());

          if (selectedLocation != "All")
            {
              console.log(selectedLocation)
              userData = userData.filter((item) =>
                item.location == selectedLocation
              )
            }
          setUserDataList(userData);
        })

        return () => {
        unsubscribe()
        }
    }, [selectedLocation])


  return (
    <Box sx={{ flexGrow: 1, maxWidth: 752 }}>

        {/* Title */}
        <ListItem>
            <Typography
                component="h1"
                variant="h7"
                color="inherit"
                noWrap
                sx={{ flexGrow: 1, ml:2, mr: 0, fontWeight: 'bold' }}
            >
              Data Status
            </Typography>
            <Typography
                component="h1"
                variant="h7"
                color="inherit"
                noWrap
                sx={{
                    flexGrow: 1,
                    mr: 6,
                    textAlign: 'center',
                    backgroundColor: '#E0EDFB',
                    padding: '1px 1px',
                  }}
            >
                FINTECH
              </Typography>

              <Button
                endIcon={<MoreHorizIcon />}
                sx={{
                  flexGrow: 1,
                  color: 'black',
                  justifyContent: 'flex-end',
                }}
                href="/Dashboard/Finance/DataSelection"
              >
              </Button>
        </ListItem>

        {/* List of data status shown */}
        <Box sx={{ height: 160, overflow: 'auto' }}>
        {userDataList.length > 0 ? (
            <List>
              {userDataList.map((row) => (
                <Paper elevation={2} sx={{ height: 45,mt: 0, ml: 2, mb: 2, mr:2 }}>
                  <ListItem sx={{ mt: -1, mb: -1 }}
                      secondaryAction={
                          <ListItemText
                            primary={row.status}
                            sx={{
                              color: row.status == 'On Track' ? 'green' : 'red',
                              fontWeight: 'bold',
                            }}
                          />
                      }
                  >
                      <ListItemText
                          primary={row.name}
                      />
                  </ListItem>
                </Paper>
              ))}
            </List>
              ): (
              <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column', height: '100%',  }}>
                  <Typography 
                      component="h1" 
                      variant="h7" 
                      sx={{ 
                          mt: 2, textAlign: 'center' 
                      }}>
                          No metrics selected or no data matched for current location. Please select metrics in Finance - Goal Metrics Page.
                  </Typography>
              </Paper>
              )
            }
            
        </Box>
    </Box>
  );
}
</file>

<file path="src/OverviewPageComponents/FinancialMetricsTable.js">
import * as React from 'react';
import { useTheme } from '@mui/material/styles';
import { LineChart, Line, XAxis,YAxis, Label, ResponsiveContainer } from 'recharts';
import {Paper,Typography} from '@mui/material';


export default function FinancialMetricsTable({metricValue, metricUnit, metricName, paperwide, paperHeight}) {
    const theme = useTheme();
    
    return (

    <Paper
        sx={{
        p: 1,
        ml:2,
        mr:2,
        display: 'flex',
        flexDirection: 'column',
        height: `${paperHeight}px`,
        minWidth: `${paperwide}px`
        }}
    >

        <Typography
            component="h1"
            variant="h7"
            color="inherit"
            noWrap
            sx={{ flexGrow: 1, ml: 1,  fontWeight: 'bold' }}
        >
            {metricName}
        </Typography>
        <ResponsiveContainer>
            <LineChart
                data={metricValue}
                margin={{
                top: 16,
                right: 16,
                bottom: 0,
                left: 24,
                }}
            >
                <XAxis
                    dataKey="time"
                    stroke={theme.palette.text.secondary}
                    style={theme.typography.body2}
                    axisLine={ false }
                    tickLine={ false }
                />
                    <YAxis
                    stroke={theme.palette.text.secondary}
                    style={theme.typography.body2}
                    axisLine={false}
                    tickLine={false}
                >
                    {metricUnit && (
                        <Label
                        value={"Amount (" + metricUnit + ")"}
                        position="insideLeft"
                        angle={-90}
                        offset={-5}
                        style={{ textAnchor: 'middle', fontSize:15 }}
                        />
                    )}
                </YAxis>
                <Line
                    isAnimationActive={false}
                    type="monotone"
                    dataKey="amount"
                    stroke={theme.palette.primary.main}
                    dot={false}
                />
            </LineChart>
        </ResponsiveContainer>
    </Paper>

    )
}
</file>

<file path="src/OverviewPageComponents/operationalMetricsTable.js">
import * as React from 'react';
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import MoreHorizIcon from '@mui/icons-material/MoreHoriz';

// Main function of this page
export default function OperationalMetricsTable({ dateRange, operationalMetricsList }) {

  return (
    <Box sx={{ flexGrow: 1, maxWidth: 1504 }}>

        {/* Title */}
        <ListItem>
            <Typography
                component="h1"
                variant="h7"
                color="inherit"
                noWrap
                sx={{ mr: 5, fontWeight: 'bold' }}
            >
              Operational Metrics
            </Typography>
            <Typography
                component="h1"
                variant="h7"
                color="inherit"
                noWrap
                sx={{
                    flexGrow: 1,
                    ml: 1,
                    mr: 40,
                    textAlign: 'center',
                    backgroundColor: '#E0EDFB',
                    padding: '1px 1px',
                  }}
            >
                DEEP TECH
              </Typography>
              
              <Button
                endIcon={<MoreHorizIcon />}
                sx={{
                  flexGrow: 1,
                  color: 'black',
                  justifyContent: 'flex-end',
                }}
                href="/Dashboard/Finance/Planning"
              >

              </Button>
        </ListItem>

        {/* List of data status shown */}
        <Box sx={{  overflowX: 'auto' }}>
          <List sx={{ display: 'flex' }}>
            {operationalMetricsList.length > 0 ? (
                operationalMetricsList?.map((row) => (
                  <Paper elevation={3} sx={{  mt:-1, ml: 2, mb: 2, mr:2, minWidth: 220, height: 150 }}>
                    <Box display="flex" alignItems="center">
                        <Typography
                          variant="h4"
                          component="div"
                          sx={{
                            fontSize: '32px',
                            mt:2,
                            ml:2,
                            color: '#1F8EFA',
                          }}
                        >
                          {row.metricValue}
                        </Typography>
                        <Typography
                          variant="h5"
                          component="div"
                          sx={{
                            fontSize: '26px',
                            mt:2,
                            ml:1,
                            color: '#1F8EFA',
                          }}
                        >
                          {row.unit}
                        </Typography>
                      </Box>

                    <ListItemText
                      primary={row.name}
                      primaryTypographyProps={{
                        style: {
                          fontWeight: 'bold',
                        },
                      }}
                      sx={{
                        ml: 2,
                      }}
                    />
                    <ListItemText
                      primary= {dateRange.start ? dateRange.start + ' - ' + dateRange.end : ""} 
                      sx={{
                        color: "#999999",
                        ml: 2,
                      }}
                    />
                  </Paper>
                ))):(
                  <Typography 
                  component="h1" 
                  variant="h6" 
                  sx={{ 
                     ml:30, mt: 2, textAlign: 'center' 
                  }}>
                      No existing operational metrics.
                 </Typography>
                )}
          </List>
        </Box>
    </Box>
  );
}
</file>

<file path="src/OverviewPageComponents/recommendationTable.js">
import * as React from 'react';
import { styled } from '@mui/material/styles';
import {Typography,  Paper, Grid, Box,List, ListItem, ListItemText,
        ListItemIcon, ListItemButton,CircularProgress 
    } from '@mui/material';
import { useState, useEffect } from "react";
import { getFirestore, collection, onSnapshot, query, limit, orderBy, where } from 'firebase/firestore'
import AccessTimeIcon from '@mui/icons-material/AccessTime';
import PaidIcon from '@mui/icons-material/Paid';
import StorageIcon from '@mui/icons-material/Storage';
import ArrowForwardIcon from '@mui/icons-material/ArrowForward';
import firebaseApp  from "../firebase-config"


// Connect to current firebase project
const firestore = getFirestore(firebaseApp);

const Demo = styled('div')(({ theme }) => ({
    backgroundColor: "rgba(158,159,173,0.13)",
}));

/* Identify the current user */
const user_email = window.localStorage.getItem('user_email');

const ProgressWrapper = styled('div')({
    position: 'relative',
    marginLeft: '60px',
    marginTop: '20px'
  });
  
  const ProgressValue = styled(Typography)({
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    fontSize: '1rem',
  });



// Main function of this page
export default function RecommendationTable({metricId}) {
    const [recommendations, setRecommendations] = useState([])
    const [filteredRecommendations, setFilteredRecommendations] = useState([])

    const industry = window.localStorage.getItem('industry');

    /* Firestore SDK queries */
    useEffect(() => {
        const recommedationsQuery = query(
            collection(firestore, 'recommendations'),
            where('user_email', '==', user_email),
            where('industry', '==', industry)
        );
      
        const unsubscribe = onSnapshot(recommedationsQuery, (snapshot) => {
          const data = snapshot.docs.map((doc) => ({ id: doc.id, data: doc.data() }));
          setRecommendations(data);
      
          if (metricId !== 0) {
            const filteredData = data.filter((item) =>
              item.data.metricId.includes(metricId)
            );
            setFilteredRecommendations(filteredData);
          } else {
            setFilteredRecommendations(data);
          }
        });
      
        return () => unsubscribe();
      }, [metricId]);

    return (
        
        <Box sx={{ flexGrow: 1, maxWidth: 1504 }}>
            {/* Title */}
            <ListItem>
                <Typography
                    component="h1"
                    variant="h7"
                    color="inherit"
                    noWrap
                    sx={{ flexGrow: 1,fontWeight: 'bold', ml:2, mr: 3 }}
                >
                    Recommendations
                </Typography>
                
                <Typography
                    component="h1"
                    variant="h7"
                    color="inherit"
                    noWrap
                    sx={{
                        flexGrow: 1,
                        mt: 0,
                        ml: 1,
                        mb: 0,
                        textAlign: 'center',
                        backgroundColor: '#E0EDFB',
                        padding: '1px 1px',
                    }}
                >
                    FINTECH
                </Typography>
                <Box sx={{ width: 820 }}></Box>
            </ListItem>
            
            {/* List of recommendations shown by SDKs */}
            <Box sx={{ maxHeight: 150, overflow: 'auto' }}>
                
                <List>
                {filteredRecommendations.length > 0 ? (
                    filteredRecommendations.map((row) => (
                        <Paper elevation={3} sx={{  mt:-1, ml: 4, mb: 2, mr:2 }}>
                            <Grid container>
                                {/* recommendation details */}
                                <Grid item xs={9}>
                                    <Typography 
                                        component="h1"
                                        variant="h7"
                                        color='#1F8EFA'
                                        fontWeight='bold'
                                        sx={{
                                            mt: 2,
                                            ml: 2,
                                            
                                        }}
                                    >
                                        {row.data.description}
                                    </Typography>
                            
                                    {/* <Typography 
                                        variant="subtitle1"
                                        sx={{
                                            mt: 0,
                                            ml: 2,
                                            mb: 1,
                                        }}
                                    >
                                        {row.data.subtitle}
                                    </Typography> */}

                                    <Typography 
                                        variant="body1"
                                        sx={{
                                            mt: 3,
                                            ml: 2,
                                            mb: 1,
                                        }}
                                    >
                                    <Grid container direction="row" alignItems="center">
                                        <ListItemIcon sx={{ fontSize: 'small', mr:-3 }}>
                                            <AccessTimeIcon />
                                        </ListItemIcon>
                                        <ListItemText primary={`Timeline: ${row.data.timeline}`} sx={{ fontSize: 'small' }} />
                                        <ListItemIcon sx={{ fontSize: 'small', mr:-3 }}>
                                            <PaidIcon />
                                        </ListItemIcon>
                                        <ListItemText primary={`Monthly Financial Impact: ${row.data.monthlyImpact}`} sx={{ fontSize: 'small'}} />
                                        <ListItemIcon sx={{ fontSize: 'small', mr:-3 }}>
                                            <StorageIcon />
                                        </ListItemIcon>
                                        <ListItemText primary={`Data Feeds Connected: ${row.data.dataFeedsConnected}`} sx={{ fontSize: 'small'}} />
  
                                    </Grid>
                                    </Typography>
                                </Grid>

                                {/* Progress Indicator */}
                                <Grid item xs={3} container justify="flex-end" alignItems="center">
                                    <ProgressWrapper>
                                        <CircularProgress 
                                            variant="determinate"
                                            value={parseInt(row.data.confidence, 10)}
                                            size={50}
                                            thickness={3}
                                        />
                                        <ProgressValue>{row.data.confidence}</ProgressValue>
                                    </ProgressWrapper>
                                    <[Third party]"" >
                                        <ListItemText primary="PROGRESS DETAILS" sx={{ color: '#0074FF', fontSize: '10px' }} />
                                        <ListItemIcon >
                                        <ArrowForwardIcon sx={{ color: '#0074FF' }}/>
                                        </ListItemIcon>
                                    </ListItemButton>
                                    
                                </Grid>
                            </Grid>
                        </Paper>
                    ))):
                    (
                    <Typography 
                    component="h1" 
                    variant="h6" 
                    sx={{ 
                        mt: 2, textAlign: 'center' 
                    }}>
                        No existing recommendations.
                    </Typography>
                    )
                }
                </List>
            </Box>
        </Box>
    );
}
</file>

<file path="src/pics/AmbientLogo_Colour-01.svg">
<svg id="Shapes" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 946.75 440.25"><defs><style>.cls-1{fill:#021059;}.cls-2{fill:#0086bb;}.cls-3{fill:#00b4fa;}.cls-4{fill:#0098d3;}.cls-5{fill:#00abed;}.cls-6{fill:#70d6f1;}.cls-7{fill:#05c5f8;}</style></defs><path class="cls-1" d="M442.14,116h16.55l24.77,70H467.6L463,171.64H437.2L432.45,186H417.14Zm-1,43.56H459.1L450.26,132Z"/><path class="cls-1" d="M538.81,116h21.05v70H546.23V138.68c0-1.36,0-3.27,0-5.72s.05-4.35.05-5.68L533.06,186H518.84l-13.17-58.76c0,1.33,0,3.22,0,5.68s.05,4.36.05,5.72V186H492.13V116h21.29l12.74,55.05Z"/><path class="cls-1" d="M625.62,123.48a17.83,17.83,0,0,1,3.21,10.69q0,6.41-3.24,10.3a16.68,16.68,0,0,1-5.34,4,15.56,15.56,0,0,1,8.08,6.18,18.52,18.52,0,0,1,2.74,10.26A20.44,20.44,0,0,1,628,176.06a19.31,19.31,0,0,1-12.87,9,48.76,48.76,0,0,1-9.89.95H573.64V116h33.83Q620.28,116.22,625.62,123.48Zm-38,4.7v15.44h17a14.16,14.16,0,0,0,7.41-1.73q2.84-1.74,2.84-6.16,0-4.89-3.76-6.46a26.66,26.66,0,0,0-8.28-1.09Zm0,27v18.67h17a16.55,16.55,0,0,0,7.09-1.24q4.6-2.28,4.6-8.74c0-3.64-1.49-6.14-4.45-7.5a17.73,17.73,0,0,0-7-1.19Z"/><path class="cls-1" d="M657,186H642.47V116H657Z"/><path class="cls-1" d="M722.45,128.42h-37v14.87h34v12.16h-34v18h38.75V186h-53V116h51.34Z"/><path class="cls-1" d="M735.33,116h15.33l27.8,48.82V116h13.63v70H777.46L749,136.36V186H735.33Z"/><path class="cls-1" d="M856.69,116v12.4h-21V186H821V128.42H800V116Z"/><path class="cls-1" d="M432.66,254.22q.68,4.8,2.67,7.18,3.63,4.32,12.46,4.32a26.88,26.88,0,0,0,8.59-1.14q6.25-2.19,6.25-8.12a6,6,0,0,0-3.06-5.37c-2-1.24-5.29-2.33-9.72-3.28l-7.58-1.66q-11.19-2.47-15.36-5.37-7.08-4.84-7.08-15.15A20.12,20.12,0,0,1,426.76,210q6.93-6.23,20.34-6.22,11.19,0,19.11,5.87t8.3,17H460.45q-.39-6.31-5.66-9a19.33,19.33,0,0,0-8.71-1.76q-5.81,0-9.25,2.28a7.23,7.23,0,0,0-3.46,6.37,6,6,0,0,0,3.41,5.6q2.19,1.23,9.31,2.9L458.37,236q8.08,1.91,12.11,5.09,6.25,4.94,6.26,14.29a20.08,20.08,0,0,1-7.42,15.94q-7.43,6.34-20.95,6.34-13.85,0-21.75-6.24t-7.93-17.18Z"/><path class="cls-1" d="M527,205.82h16.57l-23.41,43.77v26.25H505.48V249.59l-24.23-43.77h17.24L513,236.32Z"/><path class="cls-1" d="M562.43,254.22q.68,4.8,2.67,7.18,3.63,4.32,12.46,4.32a26.88,26.88,0,0,0,8.59-1.14q6.26-2.19,6.25-8.12a6,6,0,0,0-3.06-5.37q-3.08-1.86-9.72-3.28L572,246.15q-11.19-2.47-15.36-5.37-7.08-4.84-7.08-15.15A20.12,20.12,0,0,1,556.53,210q6.93-6.23,20.34-6.22,11.19,0,19.11,5.87t8.3,17H590.22q-.4-6.31-5.66-9a19.33,19.33,0,0,0-8.71-1.76q-5.8,0-9.25,2.28a7.23,7.23,0,0,0-3.46,6.37,6,6,0,0,0,3.41,5.6q2.19,1.23,9.3,2.9L588.14,236q8.07,1.91,12.11,5.09,6.25,4.94,6.26,14.29a20.08,20.08,0,0,1-7.42,15.94q-7.43,6.34-21,6.34-13.83,0-21.74-6.24t-7.93-17.18Z"/><path class="cls-1" d="M667.64,205.82v12.4H646.69v57.62H632V218.22h-21v-12.4Z"/><path class="cls-1" d="M728,218.22h-37v14.87h34v12.16h-34v18h38.75v12.59h-53v-70H728Z"/><path class="cls-1" d="M787.52,205.82h21.05v70H794.94V228.48c0-1.36,0-3.27,0-5.72s0-4.35,0-5.68l-13.26,58.76H767.55l-13.18-58.76c0,1.33,0,3.22,0,5.68s.05,4.36.05,5.72v47.36H740.84v-70h21.29l12.74,55.05Z"/><path class="cls-1" d="M832.65,254.22q.69,4.8,2.67,7.18,3.63,4.32,12.46,4.32a26.84,26.84,0,0,0,8.59-1.14q6.25-2.19,6.26-8.12a6,6,0,0,0-3.07-5.37c-2-1.24-5.29-2.33-9.72-3.28l-7.57-1.66q-11.19-2.47-15.36-5.37-7.08-4.84-7.08-15.15A20.09,20.09,0,0,1,826.76,210q6.91-6.23,20.33-6.22,11.2,0,19.11,5.87t8.3,17H860.44q-.39-6.31-5.65-9a19.37,19.37,0,0,0-8.72-1.76q-5.79,0-9.24,2.28a7.21,7.21,0,0,0-3.46,6.37,6,6,0,0,0,3.41,5.6q2.19,1.23,9.3,2.9L858.37,236q8.07,1.91,12.1,5.09,6.25,4.94,6.26,14.29a20.1,20.1,0,0,1-7.41,15.94q-7.43,6.34-21,6.34-13.83,0-21.75-6.24t-7.92-17.18Z"/><path class="cls-1" d="M440.29,299.29a10.1,10.1,0,0,1,3.27,6.46H439.8a7.16,7.16,0,0,0-7.76-6,8.35,8.35,0,0,0-6.66,2.95c-1.7,2-2.54,5-2.54,9.07a13.32,13.32,0,0,0,2.29,8.11A8,8,0,0,0,432,323a7.19,7.19,0,0,0,6.37-3.27,12.45,12.45,0,0,0,1.73-4.54h3.76a12.93,12.93,0,0,1-3.29,7.54,11.65,11.65,0,0,1-9,3.66,11.84,11.84,0,0,1-8.23-3q-4.38-4-4.38-12.27a15.77,15.77,0,0,1,3.29-10.33,12,12,0,0,1,9.82-4.38Q437.34,296.44,440.29,299.29Z"/><path class="cls-1" d="M448.44,297.21h3.49v28.45h-3.49Z"/><path class="cls-1" d="M457.16,297.21h3.54v4h-3.54Zm0,7.81h3.54v20.64h-3.54Z"/><path class="cls-1" d="M466,304.92h3.45v2.95a11.34,11.34,0,0,1,2.24-2.23,6.76,6.76,0,0,1,3.92-1.18,6.13,6.13,0,0,1,4,1.22,6.55,6.55,0,0,1,1.55,2.05,7.2,7.2,0,0,1,6.25-3.27c2.79,0,4.69,1,5.7,3a9.88,9.88,0,0,1,.81,4.37v13.81h-3.62V311.25a3.34,3.34,0,0,0-1-2.84,4.08,4.08,0,0,0-2.53-.78,5,5,0,0,0-3.53,1.38q-1.49,1.37-1.48,4.59v12.06h-3.55V312.13a7,7,0,0,0-.5-3.08,3.07,3.07,0,0,0-3-1.46,5.13,5.13,0,0,0-3.6,1.53q-1.6,1.53-1.61,5.54v11H466Z"/><path class="cls-1" d="M510.13,313.11a1.9,1.9,0,0,0,1.61-1,3.22,3.22,0,0,0,.23-1.35,2.83,2.83,0,0,0-1.27-2.59,6.72,6.72,0,0,0-3.62-.81,4.58,4.58,0,0,0-3.87,1.48,5,5,0,0,0-.83,2.43h-3.25q.09-3.84,2.48-5.35a10.23,10.23,0,0,1,5.55-1.5,11.24,11.24,0,0,1,5.93,1.39,4.74,4.74,0,0,1,2.27,4.34v12a1.52,1.52,0,0,0,.22.87,1.07,1.07,0,0,0,.94.33l.52,0,.62-.08v2.57a8.8,8.8,0,0,1-1.24.29,8.7,8.7,0,0,1-1.16.06,2.86,2.86,0,0,1-2.61-1.28,4.72,4.72,0,0,1-.6-1.91,9,9,0,0,1-3.06,2.42,9.53,9.53,0,0,1-4.4,1,6.55,6.55,0,0,1-4.72-1.75,5.82,5.82,0,0,1-1.83-4.38,5.65,5.65,0,0,1,1.8-4.47,8.56,8.56,0,0,1,4.73-1.95Zm-7.34,9.42a4.09,4.09,0,0,0,2.61.87,8.07,8.07,0,0,0,3.57-.85,4.79,4.79,0,0,0,2.9-4.62v-2.81a5.87,5.87,0,0,1-1.64.68,14.58,14.58,0,0,1-2,.39l-2.11.27a8.27,8.27,0,0,0-2.85.79,3.09,3.09,0,0,0-1.62,2.9A2.86,2.86,0,0,0,502.79,322.53Z"/><path class="cls-1" d="M521.77,299.13h3.52v5.79h3.32v2.85h-3.32v13.54a1.47,1.47,0,0,0,.74,1.45,3.17,3.17,0,0,0,1.36.21h.54a6.83,6.83,0,0,0,.68-.07v2.77a8.39,8.39,0,0,1-1.25.26A12.43,12.43,0,0,1,526,326c-1.62,0-2.73-.41-3.31-1.25a5.54,5.54,0,0,1-.87-3.24V307.77H519v-2.85h2.81Z"/><path class="cls-1" d="M544.91,305.49a7.91,7.91,0,0,1,3.13,2.68,9.21,9.21,0,0,1,1.39,3.67,24.4,24.4,0,0,1,.31,4.57H534.65a9,9,0,0,0,1.48,5.08,4.94,4.94,0,0,0,4.28,1.91,5.54,5.54,0,0,0,4.33-1.81,6.18,6.18,0,0,0,1.28-2.43h3.43a7.15,7.15,0,0,1-.9,2.54,9,9,0,0,1-1.71,2.3,8,8,0,0,1-3.9,2.09,11.68,11.68,0,0,1-2.83.31,8.63,8.63,0,0,1-6.52-2.82q-2.69-2.82-2.68-7.89a12,12,0,0,1,2.7-8.12,8.87,8.87,0,0,1,7-3.11A9.41,9.41,0,0,1,544.91,305.49Zm1.24,8.15a9,9,0,0,0-1-3.63,5,5,0,0,0-4.74-2.51,5.23,5.23,0,0,0-4,1.73,6.54,6.54,0,0,0-1.71,4.41Z"/><path class="cls-1" d="M571.74,297.21h4.36l10.32,28.45H582.2l-2.89-8.52H568.06L565,325.66h-4ZM578.07,314l-4.32-12.57L569.16,314Z"/><path class="cls-1" d="M590.16,299.13h3.52v5.79H597v2.85h-3.31v13.54a1.47,1.47,0,0,0,.74,1.45,3.14,3.14,0,0,0,1.35.21h.55a6.38,6.38,0,0,0,.67-.07v2.77a8.26,8.26,0,0,1-1.24.26,12.55,12.55,0,0,1-1.41.07c-1.63,0-2.73-.41-3.31-1.25a5.54,5.54,0,0,1-.87-3.24V307.77h-2.81v-2.85h2.81Z"/><path class="cls-1" d="M609.07,297.21h4.5l8.18,13.68,8.18-13.68h4.53l-10.78,17v11.46h-3.85V314.2Z"/><path class="cls-1" d="M648.65,307q2.75,2.67,2.75,7.86a13.57,13.57,0,0,1-2.42,8.28q-2.43,3.27-7.52,3.27a8.44,8.44,0,0,1-6.75-2.89,11.46,11.46,0,0,1-2.5-7.77c0-3.49.87-6.26,2.63-8.32a8.82,8.82,0,0,1,7.08-3.1A9.3,9.3,0,0,1,648.65,307Zm-2.17,13.79a13.16,13.16,0,0,0,1.28-5.83,10.49,10.49,0,0,0-.92-4.72,5.16,5.16,0,0,0-5-2.87,4.91,4.91,0,0,0-4.59,2.44,11.34,11.34,0,0,0-1.44,5.88,9.86,9.86,0,0,0,1.44,5.51,5,5,0,0,0,4.55,2.21C644.07,323.4,645.64,322.52,646.48,320.78Z"/><path class="cls-1" d="M659.17,304.92v13.77a5.91,5.91,0,0,0,.49,2.6,3.4,3.4,0,0,0,3.37,1.86,4.77,4.77,0,0,0,4.83-3.26,13.08,13.08,0,0,0,.7-4.78V304.92h3.49v20.74h-3.3l0-3.06a6.88,6.88,0,0,1-1.65,2,7.23,7.23,0,0,1-4.75,1.63q-4.35,0-5.93-3a9,9,0,0,1-.86-4.24v-14.1Z"/><path class="cls-1" d="M677.84,304.92h3.31v3.58a8.06,8.06,0,0,1,2-2.54,5.18,5.18,0,0,1,3.66-1.5,2.33,2.33,0,0,1,.33,0l.8.07v3.68a4.41,4.41,0,0,0-.57-.07,5.24,5.24,0,0,0-.57,0,5,5,0,0,0-4,1.69,5.88,5.88,0,0,0-1.42,3.9v11.93h-3.48Z"/><path class="cls-1" d="M705,316.48a8.12,8.12,0,0,0,1.1,3.94q1.85,2.82,6.51,2.82a11,11,0,0,0,3.81-.62q3.32-1.2,3.32-4.3a3.76,3.76,0,0,0-1.41-3.31,13.82,13.82,0,0,0-4.46-1.68l-3.74-.87a16.72,16.72,0,0,1-5.17-1.88,6,6,0,0,1-2.63-5.33,8.3,8.3,0,0,1,2.58-6.29q2.58-2.46,7.31-2.46a12.44,12.44,0,0,1,7.4,2.16q3,2.16,3,6.9H719a7.39,7.39,0,0,0-1.18-3.51q-1.69-2.22-5.74-2.22c-2.18,0-3.75.47-4.7,1.43a4.6,4.6,0,0,0-1.43,3.33,3.26,3.26,0,0,0,1.69,3.06,23.87,23.87,0,0,0,5,1.55l3.87.91a11.66,11.66,0,0,1,4.31,1.8,6.83,6.83,0,0,1,2.63,5.79c0,3.15-1.12,5.41-3.35,6.76a14.73,14.73,0,0,1-7.8,2c-3.45,0-6.15-.91-8.1-2.71a9.28,9.28,0,0,1-2.87-7.31Z"/><path class="cls-1" d="M741.24,305.49a7.94,7.94,0,0,1,3.14,2.68,9.35,9.35,0,0,1,1.38,3.67,23.56,23.56,0,0,1,.31,4.57H731a9,9,0,0,0,1.48,5.08,5,5,0,0,0,4.29,1.91,5.52,5.52,0,0,0,4.32-1.81,6.18,6.18,0,0,0,1.28-2.43h3.43a7.15,7.15,0,0,1-.9,2.54,9,9,0,0,1-1.71,2.3,8,8,0,0,1-3.9,2.09,11.57,11.57,0,0,1-2.83.31,8.65,8.65,0,0,1-6.52-2.82q-2.67-2.82-2.67-7.89a12,12,0,0,1,2.69-8.12,8.89,8.89,0,0,1,7-3.11A9.34,9.34,0,0,1,741.24,305.49Zm1.25,8.15a9.19,9.19,0,0,0-1-3.63,5,5,0,0,0-4.75-2.51,5.26,5.26,0,0,0-4,1.73,6.54,6.54,0,0,0-1.71,4.41Z"/><path class="cls-1" d="M750.58,304.92h3.32v3.58a7.91,7.91,0,0,1,2-2.54,5.18,5.18,0,0,1,3.66-1.5,2.33,2.33,0,0,1,.33,0l.79.07v3.68a4,4,0,0,0-.57-.07,5.06,5.06,0,0,0-.57,0,5,5,0,0,0-4,1.69,5.92,5.92,0,0,0-1.41,3.9v11.93h-3.49Z"/><path class="cls-1" d="M765.41,304.92,771,321.81l5.77-16.89h3.82l-7.81,20.74H769l-7.65-20.74Z"/><path class="cls-1" d="M783.53,297.21h3.54v4h-3.54Zm0,7.81h3.54v20.64h-3.54Z"/><path class="cls-1" d="M806,306c1.47,1.13,2.35,3.09,2.65,5.86H805.3a6.25,6.25,0,0,0-1.42-3.18,4.43,4.43,0,0,0-3.54-1.27,4.88,4.88,0,0,0-4.76,3.25,12.9,12.9,0,0,0-.93,5.2,9.79,9.79,0,0,0,1.31,5.25,5.13,5.13,0,0,0,7.59.8,7.28,7.28,0,0,0,1.75-3.62h3.39c-.39,2.75-1.36,4.77-2.91,6a9.06,9.06,0,0,1-5.94,1.9,7.94,7.94,0,0,1-6.49-3,11.35,11.35,0,0,1-2.42-7.43q0-5.46,2.65-8.5a8.56,8.56,0,0,1,6.76-3A9,9,0,0,1,806,306Z"/><path class="cls-1" d="M825,305.49a7.84,7.84,0,0,1,3.13,2.68,9.21,9.21,0,0,1,1.39,3.67,23.56,23.56,0,0,1,.31,4.57H814.73a9,9,0,0,0,1.48,5.08,4.94,4.94,0,0,0,4.29,1.91,5.53,5.53,0,0,0,4.32-1.81,6.18,6.18,0,0,0,1.28-2.43h3.43a7.15,7.15,0,0,1-.9,2.54,9,9,0,0,1-1.71,2.3,8,8,0,0,1-3.9,2.09,11.62,11.62,0,0,1-2.83.31,8.65,8.65,0,0,1-6.52-2.82q-2.68-2.82-2.68-7.89a12,12,0,0,1,2.7-8.12,8.87,8.87,0,0,1,7-3.11A9.38,9.38,0,0,1,825,305.49Zm1.25,8.15a9.36,9.36,0,0,0-1-3.63,5,5,0,0,0-4.75-2.51,5.23,5.23,0,0,0-4,1.73,6.54,6.54,0,0,0-1.71,4.41Z"/><polygon class="cls-2" points="338.76 314.38 234.58 318.11 93.48 92.72 199.97 92.72 338.76 314.38"/><path class="cls-3" d="M200,92.77c-.81,0-1.62-.06-2.44-.06a51.73,51.73,0,0,0-51.73,51.73V370.23H70V147.92h0c0-.69,0-1.37,0-2.06A75.85,75.85,0,0,1,200,92.77Z"/><polygon class="cls-4" points="297.26 248.11 311.09 270.2 285.05 271.13 259 272.07 271.22 249.05 283.43 226.02 297.26 248.11"/><polygon class="cls-4" points="220.75 296.02 206.91 273.94 232.96 273 259 272.07 246.79 295.09 234.58 318.11 220.75 296.02"/><polygon class="cls-5" points="272.84 294.16 259 272.07 285.05 271.13 311.09 270.2 298.88 293.22 286.67 316.25 272.84 294.16"/><polygon class="cls-3" points="324.93 292.29 338.76 314.38 312.71 315.31 286.67 316.25 298.88 293.22 311.09 270.2 324.93 292.29"/><polygon class="cls-6" points="358.07 345.61 371.9 367.69 345.86 368.63 319.81 369.56 332.03 346.54 344.24 323.52 358.07 345.61"/><polygon class="cls-3" points="272.84 294.16 286.67 316.25 260.62 317.18 234.58 318.11 246.79 295.09 259 272.07 272.84 294.16"/><polygon class="cls-6" points="300.5 338.33 286.67 316.25 312.71 315.31 338.76 314.38 326.54 337.4 314.33 360.42 300.5 338.33"/><polygon class="cls-7" points="300.5 338.33 314.33 360.42 288.29 361.36 262.24 362.29 274.45 339.27 286.67 316.25 300.5 338.33"/><polygon class="cls-5" points="248.41 340.2 234.58 318.11 260.62 317.18 286.67 316.25 274.45 339.27 262.24 362.29 248.41 340.2"/></svg>
</file>

<file path="src/pics/aws_logo.svg">
<?xml version="1.0" encoding="UTF-8"?>
<!-- Uploaded to: SVG Repo, www.svgrepo.com, Generator: SVG Repo Mixer Tools -->
<svg width="800px" height="800px" viewBox="0 -51.5 256 256" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" preserveAspectRatio="xMidYMid">
		<g>
				<path d="M72.392053,55.4384106 C72.392053,58.5748344 72.7311258,61.1178808 73.3245033,62.9827815 C74.002649,64.8476821 74.8503311,66.8821192 76.0370861,69.0860927 C76.4609272,69.7642384 76.6304636,70.4423841 76.6304636,71.0357616 C76.6304636,71.8834437 76.1218543,72.7311258 75.0198675,73.5788079 L69.6794702,77.1390728 C68.9165563,77.6476821 68.1536424,77.9019868 67.4754967,77.9019868 C66.6278146,77.9019868 65.7801325,77.4781457 64.9324503,76.7152318 C63.7456954,75.4437086 62.7284768,74.0874172 61.8807947,72.7311258 C61.0331126,71.2900662 60.1854305,69.6794702 59.2529801,67.7298013 C52.6410596,75.5284768 44.3337748,79.4278146 34.3311258,79.4278146 C27.210596,79.4278146 21.5311258,77.3933775 17.3774834,73.3245033 C13.2238411,69.2556291 11.1046358,63.8304636 11.1046358,57.0490066 C11.1046358,49.8437086 13.6476821,43.994702 18.818543,39.586755 C23.989404,35.1788079 30.8556291,32.9748344 39.586755,32.9748344 C42.4688742,32.9748344 45.4357616,33.2291391 48.5721854,33.6529801 C51.7086093,34.0768212 54.9298013,34.7549669 58.3205298,35.5178808 L58.3205298,29.3298013 C58.3205298,22.8874172 56.9642384,18.394702 54.3364238,15.7668874 C51.6238411,13.1390728 47.0463576,11.8675497 40.5192053,11.8675497 C37.5523179,11.8675497 34.5006623,12.2066225 31.3642384,12.9695364 C28.2278146,13.7324503 25.1761589,14.6649007 22.2092715,15.8516556 C20.8529801,16.4450331 19.8357616,16.784106 19.2423841,16.9536424 C18.6490066,17.1231788 18.2251656,17.207947 17.8860927,17.207947 C16.6993377,17.207947 16.1059603,16.3602649 16.1059603,14.5801325 L16.1059603,10.4264901 C16.1059603,9.07019868 16.2754967,8.05298013 16.6993377,7.45960265 C17.1231788,6.86622517 17.8860927,6.27284768 19.0728477,5.6794702 C22.0397351,4.15364238 25.6,2.88211921 29.7536424,1.86490066 C33.9072848,0.762913907 38.3152318,0.254304636 42.9774834,0.254304636 C53.0649007,0.254304636 60.4397351,2.54304636 65.186755,7.1205298 C69.8490066,11.6980132 72.2225166,18.6490066 72.2225166,27.9735099 L72.2225166,55.4384106 L72.392053,55.4384106 Z M37.9761589,68.3231788 C40.7735099,68.3231788 43.6556291,67.8145695 46.7072848,66.797351 C49.7589404,65.7801325 52.4715232,63.9152318 54.7602649,61.3721854 C56.1165563,59.7615894 57.1337748,57.981457 57.6423841,55.9470199 C58.1509934,53.9125828 58.4900662,51.4543046 58.4900662,48.5721854 L58.4900662,45.0119205 C56.0317881,44.418543 53.4039735,43.9099338 50.6913907,43.5708609 C47.9788079,43.2317881 45.3509934,43.0622517 42.7231788,43.0622517 C37.0437086,43.0622517 32.8900662,44.1642384 30.0927152,46.4529801 C27.2953642,48.7417219 25.9390728,51.9629139 25.9390728,56.2013245 C25.9390728,60.1854305 26.9562914,63.1523179 29.0754967,65.186755 C31.1099338,67.3059603 34.0768212,68.3231788 37.9761589,68.3231788 Z M106.045033,77.4781457 C104.519205,77.4781457 103.501987,77.2238411 102.823841,76.6304636 C102.145695,76.1218543 101.552318,74.9350993 101.043709,73.3245033 L81.1231788,7.7986755 C80.6145695,6.10331126 80.3602649,5.0013245 80.3602649,4.40794702 C80.3602649,3.05165563 81.0384106,2.28874172 82.394702,2.28874172 L90.7019868,2.28874172 C92.3125828,2.28874172 93.4145695,2.54304636 94.007947,3.13642384 C94.6860927,3.64503311 95.194702,4.83178808 95.7033113,6.44238411 L109.944371,62.5589404 L123.168212,6.44238411 C123.592053,4.74701987 124.100662,3.64503311 124.778808,3.13642384 C125.456954,2.62781457 126.643709,2.28874172 128.169536,2.28874172 L134.950993,2.28874172 C136.561589,2.28874172 137.663576,2.54304636 138.341722,3.13642384 C139.019868,3.64503311 139.613245,4.83178808 139.952318,6.44238411 L153.345695,63.2370861 L168.010596,6.44238411 C168.519205,4.74701987 169.112583,3.64503311 169.70596,3.13642384 C170.384106,2.62781457 171.486093,2.28874172 173.011921,2.28874172 L180.895364,2.28874172 C182.251656,2.28874172 183.01457,2.96688742 183.01457,4.40794702 C183.01457,4.83178808 182.929801,5.25562914 182.845033,5.76423841 C182.760265,6.27284768 182.590728,6.95099338 182.251656,7.88344371 L161.822517,73.4092715 C161.313907,75.1046358 160.72053,76.2066225 160.042384,76.7152318 C159.364238,77.2238411 158.262252,77.5629139 156.821192,77.5629139 L149.531126,77.5629139 C147.92053,77.5629139 146.818543,77.3086093 146.140397,76.7152318 C145.462252,76.1218543 144.868874,75.0198675 144.529801,73.3245033 L131.390728,18.6490066 L118.336424,73.2397351 C117.912583,74.9350993 117.403974,76.0370861 116.725828,76.6304636 C116.047682,77.2238411 114.860927,77.4781457 113.335099,77.4781457 L106.045033,77.4781457 Z M214.972185,79.7668874 C210.564238,79.7668874 206.156291,79.2582781 201.917881,78.2410596 C197.67947,77.2238411 194.37351,76.1218543 192.169536,74.8503311 C190.813245,74.0874172 189.880795,73.2397351 189.541722,72.4768212 C189.202649,71.7139073 189.033113,70.8662252 189.033113,70.1033113 L189.033113,65.7801325 C189.033113,64 189.711258,63.1523179 190.982781,63.1523179 C191.491391,63.1523179 192,63.2370861 192.508609,63.4066225 C193.017219,63.5761589 193.780132,63.9152318 194.627815,64.2543046 C197.509934,65.5258278 200.646358,66.5430464 203.952318,67.2211921 C207.343046,67.8993377 210.649007,68.2384106 214.039735,68.2384106 C219.380132,68.2384106 223.533775,67.3059603 226.415894,65.4410596 C229.298013,63.5761589 230.823841,60.8635762 230.823841,57.3880795 C230.823841,55.0145695 230.060927,53.0649007 228.535099,51.4543046 C227.009272,49.8437086 224.127152,48.402649 219.97351,47.0463576 L207.682119,43.2317881 C201.49404,41.2821192 196.916556,38.4 194.119205,34.5854305 C191.321854,30.8556291 189.880795,26.7019868 189.880795,22.2940397 C189.880795,18.7337748 190.643709,15.597351 192.169536,12.8847682 C193.695364,10.1721854 195.729801,7.7986755 198.272848,5.93377483 C200.815894,3.98410596 203.698013,2.54304636 207.088742,1.52582781 C210.47947,0.508609272 214.039735,0.0847682119 217.769536,0.0847682119 C219.634437,0.0847682119 221.584106,0.169536424 223.449007,0.42384106 C225.398675,0.678145695 227.178808,1.01721854 228.95894,1.35629139 C230.654305,1.78013245 232.264901,2.20397351 233.790728,2.71258278 C235.316556,3.22119205 236.503311,3.72980132 237.350993,4.2384106 C238.537748,4.91655629 239.38543,5.59470199 239.89404,6.35761589 C240.402649,7.03576159 240.656954,7.96821192 240.656954,9.15496689 L240.656954,13.1390728 C240.656954,14.9192053 239.978808,15.8516556 238.707285,15.8516556 C238.029139,15.8516556 236.927152,15.5125828 235.486093,14.8344371 C230.654305,12.6304636 225.229139,11.5284768 219.210596,11.5284768 C214.378808,11.5284768 210.564238,12.2913907 207.936424,13.9019868 C205.308609,15.5125828 203.952318,17.9708609 203.952318,21.4463576 C203.952318,23.8198675 204.8,25.8543046 206.495364,27.4649007 C208.190728,29.0754967 211.327152,30.6860927 215.819868,32.1271523 L227.856954,35.9417219 C233.960265,37.8913907 238.368212,40.6039735 240.996026,44.0794702 C243.623841,47.5549669 244.895364,51.5390728 244.895364,55.9470199 C244.895364,59.592053 244.13245,62.8980132 242.691391,65.7801325 C241.165563,68.6622517 239.131126,71.205298 236.503311,73.2397351 C233.875497,75.3589404 230.739073,76.8847682 227.09404,77.986755 C223.27947,79.1735099 219.295364,79.7668874 214.972185,79.7668874 Z" fill="#252F3E" fill-rule="nonzero">

</path>
				<path d="M230.993377,120.964238 C203.104636,141.562914 162.58543,152.498013 127.745695,152.498013 C78.9192053,152.498013 34.9245033,134.442384 1.69536424,104.434437 C-0.932450331,102.060927 1.4410596,98.8397351 4.57748344,100.704636 C40.5192053,121.557616 84.8529801,134.188079 130.712583,134.188079 C161.65298,134.188079 195.645033,127.745695 226.924503,114.521854 C231.586755,112.402649 235.570861,117.57351 230.993377,120.964238 Z M242.606623,107.740397 C239.046358,103.162914 219.04106,105.536424 209.970861,106.638411 C207.258278,106.977483 206.834437,104.603974 209.292715,102.823841 C225.229139,91.6344371 251.422517,94.8556291 254.474172,98.5854305 C257.525828,102.4 253.62649,128.593377 238.707285,141.139073 C236.418543,143.088742 234.21457,142.071523 235.231788,139.528477 C238.622517,131.136424 246.166887,112.233113 242.606623,107.740397 Z" fill="#FF9900">

</path>
		</g>
</svg>
</file>

<file path="src/pics/Logo_White-01.svg">
<svg id="Logos" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 944.89 435.62"><defs><style>.cls-1{fill:#fff;}</style></defs><path class="cls-1" d="M440.28,113.71h16.55l24.78,70H465.74l-4.62-14.39H435.34l-4.75,14.39h-15.3Zm-1,43.56h17.94l-8.85-27.55Z"/><path class="cls-1" d="M537,113.71h21v70H544.38V136.37c0-1.36,0-3.27,0-5.73s.05-4.34.05-5.67L531.2,183.72H517L503.81,125c0,1.33,0,3.22.05,5.67s.05,4.37.05,5.73v47.35H490.27v-70h21.29l12.75,55.05Z"/><path class="cls-1" d="M623.76,121.17A17.74,17.74,0,0,1,627,131.85q0,6.42-3.25,10.31a16.52,16.52,0,0,1-5.33,4,15.56,15.56,0,0,1,8.08,6.18,18.52,18.52,0,0,1,2.73,10.26,20.47,20.47,0,0,1-3.12,11.16,19.21,19.21,0,0,1-12.86,9,48.08,48.08,0,0,1-9.9.95H571.78v-70h33.84Q618.42,113.91,623.76,121.17Zm-38,4.7v15.44h17a14,14,0,0,0,7.4-1.74q2.83-1.73,2.84-6.15,0-4.89-3.76-6.46a26.3,26.3,0,0,0-8.27-1.09Zm0,27v18.66h17a16.59,16.59,0,0,0,7.09-1.23q4.59-2.28,4.6-8.74,0-5.46-4.46-7.51a17.72,17.72,0,0,0-7-1.18Z"/><path class="cls-1" d="M655.15,183.72H640.61v-70h14.54Z"/><path class="cls-1" d="M720.6,126.11H683.55V141h34v12.16h-34v18h38.76v12.58H669.25v-70H720.6Z"/><path class="cls-1" d="M733.47,113.71h15.34l27.79,48.82V113.71h13.64v70H775.61l-28.5-49.67v49.67H733.47Z"/><path class="cls-1" d="M854.83,113.71v12.4H833.89v57.61H819.16V126.11h-21v-12.4Z"/><path class="cls-1" d="M430.8,251.91q.69,4.8,2.67,7.17,3.63,4.34,12.46,4.33a26.84,26.84,0,0,0,8.59-1.14q6.25-2.19,6.26-8.13a6,6,0,0,0-3.07-5.36c-2-1.24-5.29-2.33-9.72-3.28l-7.57-1.66q-11.19-2.47-15.36-5.37Q418,233.63,418,223.32a20.09,20.09,0,0,1,6.93-15.63q6.91-6.23,20.33-6.22,11.2,0,19.12,5.86t8.29,17H458.59q-.39-6.31-5.65-9a19.24,19.24,0,0,0-8.72-1.76q-5.79,0-9.24,2.28a7.2,7.2,0,0,0-3.46,6.36,6,6,0,0,0,3.41,5.61q2.19,1.23,9.3,2.9l12.29,2.89q8.07,1.91,12.1,5.09,6.25,4.94,6.26,14.29A20.1,20.1,0,0,1,467.47,269q-7.43,6.35-21,6.34-13.83,0-21.75-6.25t-7.92-17.17Z"/><path class="cls-1" d="M525.09,203.51h16.58l-23.42,43.76v26.25H503.62V247.27L479.4,203.51h17.24L511.17,234Z"/><path class="cls-1" d="M560.57,251.91q.69,4.8,2.67,7.17,3.63,4.34,12.46,4.33a26.84,26.84,0,0,0,8.59-1.14q6.26-2.19,6.26-8.13a6,6,0,0,0-3.07-5.36c-2-1.24-5.29-2.33-9.72-3.28l-7.58-1.66q-11.17-2.47-15.35-5.37-7.08-4.84-7.08-15.15a20.09,20.09,0,0,1,6.93-15.63q6.92-6.23,20.33-6.22,11.21,0,19.11,5.86t8.3,17H588.36q-.39-6.31-5.65-9a19.24,19.24,0,0,0-8.72-1.76q-5.79,0-9.24,2.28a7.2,7.2,0,0,0-3.46,6.36,6,6,0,0,0,3.41,5.61q2.19,1.23,9.3,2.9l12.29,2.89q8.07,1.91,12.1,5.09,6.25,4.94,6.26,14.29A20.1,20.1,0,0,1,597.24,269q-7.43,6.35-21,6.34-13.83,0-21.75-6.25t-7.92-17.17Z"/><path class="cls-1" d="M665.79,203.51v12.4H644.84v57.61H630.11V215.91h-21v-12.4Z"/><path class="cls-1" d="M726.11,215.91H689.06v14.87h34v12.16h-34v18h38.76v12.58H674.76v-70h51.35Z"/><path class="cls-1" d="M785.67,203.51h21.05v70H793.09V226.17c0-1.36,0-3.27,0-5.73s0-4.34,0-5.67l-13.27,58.75H765.69l-13.17-58.75c0,1.33,0,3.22.05,5.67s0,4.37,0,5.73v47.35H739v-70h21.29L773,258.56Z"/><path class="cls-1" d="M830.8,251.91a14.2,14.2,0,0,0,2.67,7.17q3.63,4.34,12.46,4.33a26.88,26.88,0,0,0,8.59-1.14q6.26-2.19,6.25-8.13a6,6,0,0,0-3.06-5.36c-2-1.24-5.29-2.33-9.72-3.28l-7.58-1.66q-11.19-2.47-15.36-5.37Q818,233.63,818,223.32a20.12,20.12,0,0,1,6.93-15.63q6.93-6.23,20.34-6.22,11.21,0,19.11,5.86t8.3,17H858.59q-.39-6.31-5.66-9a19.2,19.2,0,0,0-8.71-1.76q-5.79,0-9.25,2.28a7.22,7.22,0,0,0-3.46,6.36,6,6,0,0,0,3.41,5.61q2.19,1.23,9.31,2.9l12.28,2.89q8.09,1.91,12.11,5.09,6.25,4.94,6.26,14.29A20.08,20.08,0,0,1,867.46,269q-7.43,6.35-21,6.34-13.85,0-21.75-6.25t-7.93-17.17Z"/><path class="cls-1" d="M438.43,297a10.12,10.12,0,0,1,3.28,6.47H438a7.14,7.14,0,0,0-7.76-6,8.37,8.37,0,0,0-6.67,2.95q-2.53,3-2.54,9.06a13.36,13.36,0,0,0,2.3,8.12,7.93,7.93,0,0,0,6.83,3.11,7.18,7.18,0,0,0,6.38-3.28,12.58,12.58,0,0,0,1.73-4.53H442a12.88,12.88,0,0,1-3.3,7.54,11.63,11.63,0,0,1-9,3.66,11.8,11.8,0,0,1-8.23-3q-4.4-4-4.39-12.26a15.81,15.81,0,0,1,3.29-10.33,12,12,0,0,1,9.82-4.38C433.7,294.13,436.47,295.07,438.43,297Z"/><path class="cls-1" d="M446.59,294.9h3.48v28.45h-3.48Z"/><path class="cls-1" d="M455.3,294.9h3.55v4H455.3Zm0,7.81h3.55v20.64H455.3Z"/><path class="cls-1" d="M464.12,302.61h3.44v2.94a11.52,11.52,0,0,1,2.25-2.22,6.74,6.74,0,0,1,3.91-1.19,6.19,6.19,0,0,1,4,1.22,6.31,6.31,0,0,1,1.55,2.06,7.24,7.24,0,0,1,6.26-3.28c2.79,0,4.68,1,5.69,3a9.88,9.88,0,0,1,.81,4.37v13.81H488.4V308.94a3.37,3.37,0,0,0-1-2.85,4.15,4.15,0,0,0-2.53-.77,5,5,0,0,0-3.54,1.38c-1,.91-1.48,2.44-1.48,4.59v12.06h-3.54V309.81a7,7,0,0,0-.51-3.08,3.08,3.08,0,0,0-3-1.45,5.11,5.11,0,0,0-3.59,1.53q-1.62,1.53-1.62,5.54v11h-3.48Z"/><path class="cls-1" d="M508.27,310.8a1.88,1.88,0,0,0,1.61-1,3,3,0,0,0,.23-1.34,2.84,2.84,0,0,0-1.26-2.59,6.76,6.76,0,0,0-3.63-.81,4.57,4.57,0,0,0-3.86,1.48,4.81,4.81,0,0,0-.83,2.43h-3.26c.07-2.56.9-4.35,2.49-5.35a10.19,10.19,0,0,1,5.54-1.5,11.26,11.26,0,0,1,5.94,1.39,4.73,4.73,0,0,1,2.26,4.34v12a1.52,1.52,0,0,0,.23.87c.14.22.46.33.94.33l.52,0,.62-.09v2.58a11,11,0,0,1-1.24.29,8.7,8.7,0,0,1-1.16.06,2.88,2.88,0,0,1-2.62-1.28,5.05,5.05,0,0,1-.6-1.92,8.81,8.81,0,0,1-3.06,2.42,9.39,9.39,0,0,1-4.4,1A6.52,6.52,0,0,1,498,322.3a5.82,5.82,0,0,1-1.83-4.38,5.65,5.65,0,0,1,1.8-4.47,8.61,8.61,0,0,1,4.73-2Zm-7.34,9.42a4.11,4.11,0,0,0,2.62.87,8,8,0,0,0,3.56-.85,4.81,4.81,0,0,0,2.91-4.63v-2.8a6.07,6.07,0,0,1-1.65.68,14.28,14.28,0,0,1-2,.39l-2.1.27a8.13,8.13,0,0,0-2.85.79,3.08,3.08,0,0,0-1.62,2.9A2.89,2.89,0,0,0,500.93,320.22Z"/><path class="cls-1" d="M519.91,296.82h3.53v5.79h3.31v2.85h-3.31V319a1.46,1.46,0,0,0,.74,1.46,3.14,3.14,0,0,0,1.35.21h.54a6.55,6.55,0,0,0,.68-.07v2.77a7.09,7.09,0,0,1-1.25.25,10.26,10.26,0,0,1-1.4.08c-1.63,0-2.73-.42-3.31-1.25a5.54,5.54,0,0,1-.88-3.24V305.46h-2.8v-2.85h2.8Z"/><path class="cls-1" d="M543.05,303.18a7.94,7.94,0,0,1,3.14,2.68,9.36,9.36,0,0,1,1.38,3.66,23.7,23.7,0,0,1,.31,4.57H532.79a9,9,0,0,0,1.48,5.08,5,5,0,0,0,4.29,1.92,5.51,5.51,0,0,0,4.32-1.81,6,6,0,0,0,1.28-2.44h3.43a7.19,7.19,0,0,1-.9,2.55,9.18,9.18,0,0,1-1.71,2.3,8,8,0,0,1-3.9,2.09,12,12,0,0,1-2.82.31,8.65,8.65,0,0,1-6.53-2.82q-2.67-2.82-2.67-7.89a12,12,0,0,1,2.69-8.12,8.88,8.88,0,0,1,7-3.12A9.35,9.35,0,0,1,543.05,303.18Zm1.25,8.14a9.14,9.14,0,0,0-1-3.62,5,5,0,0,0-4.74-2.52,5.24,5.24,0,0,0-4,1.74,6.61,6.61,0,0,0-1.71,4.4Z"/><path class="cls-1" d="M569.88,294.9h4.36l10.33,28.45h-4.23l-2.88-8.52H566.2l-3.08,8.52h-4Zm6.34,16.79-4.32-12.57-4.59,12.57Z"/><path class="cls-1" d="M588.3,296.82h3.53v5.79h3.31v2.85h-3.31V319a1.47,1.47,0,0,0,.73,1.46,3.23,3.23,0,0,0,1.36.21h.54a6.55,6.55,0,0,0,.68-.07v2.77a7.28,7.28,0,0,1-1.25.25,10.26,10.26,0,0,1-1.4.08c-1.63,0-2.73-.42-3.32-1.25a5.54,5.54,0,0,1-.87-3.24V305.46h-2.81v-2.85h2.81Z"/><path class="cls-1" d="M607.22,294.9h4.49l8.18,13.67,8.18-13.67h4.53l-10.77,17v11.46H618V311.89Z"/><path class="cls-1" d="M646.79,304.68q2.76,2.67,2.76,7.85a13.52,13.52,0,0,1-2.43,8.29q-2.42,3.27-7.52,3.27a8.5,8.5,0,0,1-6.75-2.89,11.46,11.46,0,0,1-2.5-7.77A12.42,12.42,0,0,1,633,305.1a8.8,8.8,0,0,1,7.07-3.09A9.28,9.28,0,0,1,646.79,304.68Zm-2.16,13.78a13.12,13.12,0,0,0,1.27-5.83,10.38,10.38,0,0,0-.92-4.72,5.15,5.15,0,0,0-5-2.86,4.93,4.93,0,0,0-4.6,2.44,11.34,11.34,0,0,0-1.44,5.88,9.88,9.88,0,0,0,1.44,5.51,5.05,5.05,0,0,0,4.56,2.21A4.75,4.75,0,0,0,644.63,318.46Z"/><path class="cls-1" d="M657.31,302.61v13.77a6,6,0,0,0,.49,2.59,3.41,3.41,0,0,0,3.38,1.86,4.78,4.78,0,0,0,4.83-3.25,13.33,13.33,0,0,0,.7-4.78V302.61h3.48v20.74H666.9l0-3.06a7,7,0,0,1-6.41,3.62c-2.9,0-4.88-1-5.93-3a9,9,0,0,1-.85-4.24v-14.1Z"/><path class="cls-1" d="M676,302.61h3.31v3.58a8.14,8.14,0,0,1,2-2.55,5.18,5.18,0,0,1,3.66-1.5l.33,0,.79.08v3.68c-.2,0-.39-.06-.57-.08l-.57,0a5,5,0,0,0-4,1.7,5.92,5.92,0,0,0-1.41,3.9v11.93H676Z"/><path class="cls-1" d="M703.1,314.17a7.94,7.94,0,0,0,1.1,3.93q1.84,2.83,6.51,2.83a11.28,11.28,0,0,0,3.81-.62q3.32-1.2,3.32-4.3a3.76,3.76,0,0,0-1.41-3.31A13.87,13.87,0,0,0,712,311l-3.73-.87a16.54,16.54,0,0,1-5.18-1.88,6,6,0,0,1-2.62-5.32,8.32,8.32,0,0,1,2.58-6.3q2.58-2.46,7.31-2.46a12.47,12.47,0,0,1,7.4,2.16q3,2.16,3,6.91h-3.62a7.35,7.35,0,0,0-1.19-3.51c-1.13-1.48-3-2.23-5.74-2.23q-3.27,0-4.69,1.44a4.53,4.53,0,0,0-1.43,3.33,3.29,3.29,0,0,0,1.68,3.06,24.46,24.46,0,0,0,5,1.55l3.86.91a11.72,11.72,0,0,1,4.32,1.8,6.83,6.83,0,0,1,2.62,5.79c0,3.15-1.11,5.41-3.35,6.76a14.67,14.67,0,0,1-7.79,2q-5.18,0-8.1-2.71a9.22,9.22,0,0,1-2.87-7.3Z"/><path class="cls-1" d="M739.39,303.18a7.91,7.91,0,0,1,3.13,2.68,9.22,9.22,0,0,1,1.39,3.66,24.55,24.55,0,0,1,.31,4.57H729.13a8.94,8.94,0,0,0,1.48,5.08,4.92,4.92,0,0,0,4.28,1.92,5.54,5.54,0,0,0,4.33-1.81,6.15,6.15,0,0,0,1.28-2.44h3.43a7.19,7.19,0,0,1-.9,2.55,9.43,9.43,0,0,1-1.71,2.3,8,8,0,0,1-3.9,2.09,12.2,12.2,0,0,1-2.83.31,8.63,8.63,0,0,1-6.52-2.82q-2.69-2.82-2.68-7.89a12,12,0,0,1,2.7-8.12,8.84,8.84,0,0,1,7-3.12A9.43,9.43,0,0,1,739.39,303.18Zm1.24,8.14a9,9,0,0,0-1-3.62,5,5,0,0,0-4.74-2.52,5.21,5.21,0,0,0-4,1.74,6.51,6.51,0,0,0-1.71,4.4Z"/><path class="cls-1" d="M748.73,302.61H752v3.58a8,8,0,0,1,2-2.55,5.14,5.14,0,0,1,3.66-1.5l.33,0,.79.08v3.68c-.21,0-.4-.06-.57-.08l-.57,0a5,5,0,0,0-4,1.7,5.92,5.92,0,0,0-1.41,3.9v11.93h-3.49Z"/><path class="cls-1" d="M763.56,302.61l5.53,16.89,5.78-16.89h3.81l-7.81,20.74h-3.71l-7.65-20.74Z"/><path class="cls-1" d="M781.67,294.9h3.55v4h-3.55Zm0,7.81h3.55v20.64h-3.55Z"/><path class="cls-1" d="M804.19,303.71c1.46,1.14,2.35,3.09,2.64,5.87h-3.39A6.12,6.12,0,0,0,802,306.4a4.46,4.46,0,0,0-3.54-1.27,4.9,4.9,0,0,0-4.77,3.25,12.87,12.87,0,0,0-.93,5.2,9.75,9.75,0,0,0,1.32,5.24,5.11,5.11,0,0,0,7.58.81,7.2,7.2,0,0,0,1.75-3.62h3.39q-.57,4.13-2.9,6A9,9,0,0,1,798,324a8,8,0,0,1-6.49-3,11.4,11.4,0,0,1-2.42-7.43q0-5.46,2.66-8.5a8.56,8.56,0,0,1,6.76-3A9.09,9.09,0,0,1,804.19,303.71Z"/><path class="cls-1" d="M823.13,303.18a7.94,7.94,0,0,1,3.14,2.68,9.53,9.53,0,0,1,1.39,3.66,24.76,24.76,0,0,1,.3,4.57H812.88a8.87,8.87,0,0,0,1.48,5.08,4.92,4.92,0,0,0,4.28,1.92,5.54,5.54,0,0,0,4.33-1.81,6.28,6.28,0,0,0,1.28-2.44h3.42a7.19,7.19,0,0,1-.9,2.55,9.41,9.41,0,0,1-1.7,2.3,8.12,8.12,0,0,1-3.91,2.09,12,12,0,0,1-2.82.31,8.67,8.67,0,0,1-6.53-2.82q-2.67-2.82-2.67-7.89a12,12,0,0,1,2.69-8.12,8.88,8.88,0,0,1,7-3.12A9.35,9.35,0,0,1,823.13,303.18Zm1.25,8.14a9.14,9.14,0,0,0-1-3.62,5,5,0,0,0-4.74-2.52,5.24,5.24,0,0,0-4,1.74,6.61,6.61,0,0,0-1.71,4.4Z"/><path class="cls-1" d="M142,70c-32.42,0-68.85,23.88-71.85,72.29-.21,3.38,0,223.31,0,223.31h72V141c.24-26.85,19.76-48.88,48-52.42.77-.1,2-.16,2.7-.18C179.81,75,162.11,70,142,70Z"/><path class="cls-1" d="M196.85,92.63a49.85,49.85,0,0,0-33.37,11.71c-9.46,8-17.14,19.21-17.32,38.1-.16,16.26-.1,31-.1,31,2.69,4.14,60.19,96.32,60.19,96.32l49.22-1.87L279,223.72Z"/><polygon class="cls-1" points="220.85 292.31 209.18 273.46 231.34 272.77 253.5 272.09 243.01 291.62 232.53 311.16 220.85 292.31"/><polygon class="cls-1" points="272.71 290.49 261.03 271.64 283.19 270.96 305.36 270.27 294.87 289.81 284.38 309.34 272.71 290.49"/><polygon class="cls-1" points="286.43 356.65 264.27 357.49 274.63 337.88 284.97 318.27 296.78 337.04 308.59 355.81 286.43 356.65"/><polygon class="cls-1" points="344 364.28 321.85 365.12 332.2 345.51 342.55 325.9 354.35 344.67 366.16 363.44 344 364.28"/><polygon class="cls-1" points="323.07 334.2 312.74 353.82 300.91 335.07 289.08 316.31 311.24 315.45 333.4 314.58 323.07 334.2"/><polygon class="cls-1" points="322.69 333.93 312.36 353.55 300.53 334.8 288.7 316.04 310.86 315.18 333.01 314.31 322.69 333.93"/><polygon class="cls-1" points="293.68 247.04 305.36 265.89 283.19 266.58 261.03 267.27 271.52 247.73 282.01 228.19 293.68 247.04"/><polygon class="cls-1" points="269.08 293.25 280.76 312.1 258.6 312.78 236.44 313.47 246.92 293.93 257.41 274.4 269.08 293.25"/><polygon class="cls-1" points="248.4 336.58 236.72 317.73 258.88 317.04 281.05 316.36 270.56 335.89 260.07 355.43 248.4 336.58"/><polygon class="cls-1" points="321.23 291.31 332.9 310.16 310.74 310.85 288.58 311.54 299.07 292 309.55 272.46 321.23 291.31"/></svg>
</file>

<file path="src/pics/Logo_White-03.svg">
<svg id="Logos" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600"><defs><style>.cls-1{fill:#fff;}</style></defs><path class="cls-1" d="M119.15,384.66h15.41l23.07,65.2H142.86l-4.31-13.4h-24l-4.43,13.4H95.87Zm-.9,40.56H135l-8.24-25.65Z"/><path class="cls-1" d="M209.18,384.66h19.6v65.2H216.09v-44.1c0-1.27,0-3.05,0-5.33s.05-4.05.05-5.29l-12.36,54.72H190.58l-12.27-54.72c0,1.24,0,3,.05,5.29s0,4.06,0,5.33v44.1H165.7v-65.2h19.83l11.87,51.27Z"/><path class="cls-1" d="M290,391.6a16.55,16.55,0,0,1,3,10q0,6-3,9.59a15.46,15.46,0,0,1-5,3.72,14.52,14.52,0,0,1,7.53,5.75,17.22,17.22,0,0,1,2.54,9.56,19,19,0,0,1-2.9,10.39,18,18,0,0,1-12,8.41,45.24,45.24,0,0,1-9.22.88H241.61v-65.2h31.51Q285,384.84,290,391.6ZM254.62,396v14.38h15.85a13.06,13.06,0,0,0,6.89-1.62c1.76-1.07,2.65-3,2.65-5.72q0-4.56-3.5-6a24.56,24.56,0,0,0-7.71-1Zm0,25.17v17.39h15.83a15.45,15.45,0,0,0,6.6-1.15q4.29-2.13,4.29-8.14c0-3.39-1.39-5.72-4.15-7a16.51,16.51,0,0,0-6.52-1.11Z"/><path class="cls-1" d="M319.25,449.86H305.71v-65.2h13.54Z"/><path class="cls-1" d="M380.2,396.2H345.7v13.85h31.67v11.32H345.7v16.77h36.1v11.72H332.38v-65.2H380.2Z"/><path class="cls-1" d="M392.19,384.66h14.28l25.89,45.46V384.66h12.69v65.2H431.43L404.89,403.6v46.26h-12.7Z"/><path class="cls-1" d="M505.21,384.66V396.2h-19.5v53.66H472V396.2H452.4V384.66Z"/><path class="cls-1" d="M100.26,513.36a13.23,13.23,0,0,0,2.49,6.68q3.39,4,11.6,4a25,25,0,0,0,8-1.06q5.84-2,5.83-7.57a5.57,5.57,0,0,0-2.86-5,31.1,31.1,0,0,0-9-3.05l-7-1.55q-10.43-2.29-14.31-5-6.59-4.52-6.59-14.12a18.73,18.73,0,0,1,6.45-14.55q6.45-5.79,18.94-5.79,10.42,0,17.8,5.46t7.73,15.86h-13.1a9.34,9.34,0,0,0-5.26-8.36,18,18,0,0,0-8.12-1.64,15.48,15.48,0,0,0-8.61,2.12,6.72,6.72,0,0,0-3.22,5.93,5.59,5.59,0,0,0,3.18,5.22q2,1.15,8.66,2.7l11.44,2.7q7.52,1.77,11.27,4.73,5.84,4.61,5.84,13.32a18.71,18.71,0,0,1-6.91,14.84q-6.91,5.9-19.52,5.9-12.89,0-20.25-5.81t-7.38-16Z"/><path class="cls-1" d="M188.07,468.29h15.44L181.7,509v24.45H168.08V509l-22.56-40.75h16.06l13.53,28.4Z"/><path class="cls-1" d="M221.12,513.36A13.23,13.23,0,0,0,223.6,520q3.39,4,11.61,4a25,25,0,0,0,8-1.06q5.82-2,5.82-7.57a5.58,5.58,0,0,0-2.85-5,31.29,31.29,0,0,0-9.06-3.05l-7.05-1.55q-10.42-2.29-14.31-5-6.58-4.52-6.59-14.12a18.73,18.73,0,0,1,6.45-14.55q6.45-5.79,18.94-5.79,10.44,0,17.8,5.46t7.73,15.86H247a9.32,9.32,0,0,0-5.26-8.36,18,18,0,0,0-8.12-1.64,15.5,15.5,0,0,0-8.61,2.12,6.74,6.74,0,0,0-3.22,5.93A5.59,5.59,0,0,0,225,491q2,1.15,8.66,2.7l11.44,2.7q7.53,1.77,11.28,4.73,5.82,4.61,5.83,13.32a18.71,18.71,0,0,1-6.91,14.84q-6.91,5.9-19.52,5.9-12.88,0-20.25-5.81t-7.38-16Z"/><path class="cls-1" d="M319.1,468.29v11.54H299.59v53.66H285.88V479.83h-19.6V468.29Z"/><path class="cls-1" d="M375.28,479.83H340.77v13.85h31.68V505H340.77v16.77h36.1v11.72H327.46v-65.2h47.82Z"/><path class="cls-1" d="M430.74,468.29h19.61v65.2h-12.7v-44.1c0-1.27,0-3.05.05-5.33s0-4.05,0-5.29l-12.36,54.72H412.14l-12.27-54.72c0,1.24,0,3,.05,5.29s0,4.06,0,5.33v44.1H387.27v-65.2h19.82L419,519.56Z"/><path class="cls-1" d="M472.77,513.36a13.23,13.23,0,0,0,2.49,6.68c2.25,2.69,6.13,4,11.6,4a25,25,0,0,0,8-1.06q5.83-2,5.83-7.57a5.57,5.57,0,0,0-2.86-5,31.1,31.1,0,0,0-9.05-3.05l-7.06-1.55q-10.41-2.29-14.3-5-6.59-4.52-6.59-14.12a18.73,18.73,0,0,1,6.45-14.55q6.45-5.79,18.94-5.79,10.42,0,17.8,5.46t7.73,15.86h-13.1a9.34,9.34,0,0,0-5.26-8.36,18,18,0,0,0-8.12-1.64,15.45,15.45,0,0,0-8.61,2.12,6.72,6.72,0,0,0-3.22,5.93,5.59,5.59,0,0,0,3.18,5.22q2,1.15,8.66,2.7l11.44,2.7q7.51,1.77,11.27,4.73,5.84,4.61,5.83,13.32a18.73,18.73,0,0,1-6.9,14.84q-6.92,5.9-19.52,5.9-12.88,0-20.25-5.81t-7.38-16Z"/><path class="cls-1" d="M229.64,67.08c-30.19,0-64.12,22.24-66.91,67.32-.19,3.15,0,208,0,208h67.1V133.16c.22-25,18.4-45.53,44.72-48.83.72-.09,1.85-.14,2.52-.16C264.9,71.74,248.41,67.08,229.64,67.08Z"/><path class="cls-1" d="M280.77,88.14a46.42,46.42,0,0,0-31.08,10.91c-8.81,7.49-16,17.89-16.13,35.48-.15,15.14-.1,28.88-.1,28.88,2.51,3.85,56.06,89.7,56.06,89.7l45.84-1.74,21.9-41.14Z"/><polygon class="cls-1" points="303.12 274.1 292.24 256.55 312.88 255.91 333.52 255.27 323.75 273.46 313.99 291.65 303.12 274.1"/><polygon class="cls-1" points="351.41 272.41 340.54 254.85 361.18 254.22 381.81 253.58 372.05 271.77 362.28 289.96 351.41 272.41"/><polygon class="cls-1" points="364.19 334.02 343.56 334.8 353.19 316.54 362.83 298.28 373.83 315.76 384.82 333.24 364.19 334.02"/><polygon class="cls-1" points="417.81 341.12 397.17 341.91 406.81 323.64 416.45 305.38 427.44 322.86 438.44 340.34 417.81 341.12"/><polygon class="cls-1" points="398.31 313.12 388.69 331.39 377.68 313.92 366.66 296.46 387.29 295.65 407.93 294.84 398.31 313.12"/><polygon class="cls-1" points="397.95 312.86 388.33 331.13 377.32 313.67 366.3 296.2 386.94 295.4 407.57 294.59 397.95 312.86"/><polygon class="cls-1" points="370.94 231.94 381.81 249.5 361.18 250.14 340.54 250.78 350.3 232.59 360.07 214.39 370.94 231.94"/><polygon class="cls-1" points="348.04 274.97 358.91 292.53 338.27 293.17 317.63 293.81 327.4 275.61 337.16 257.42 348.04 274.97"/><polygon class="cls-1" points="328.77 315.33 317.9 297.77 338.54 297.13 359.18 296.5 349.41 314.69 339.64 332.88 328.77 315.33"/><polygon class="cls-1" points="396.6 273.17 407.47 290.73 386.83 291.37 366.19 292.01 375.96 273.81 385.72 255.62 396.6 273.17"/></svg>
</file>

<file path="src/ProfilePage.js">
import * as React from 'react';
import { useState, useEffect } from "react";
import Box from '@mui/material/Box';
import Paper from '@mui/material/Paper';
import List from '@mui/material/List';
import ListItemText from '@mui/material/ListItemText';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Avatar from '@mui/material/Avatar';
import { useNavigate } from "react-router-dom";
import { getFirestore, collection, onSnapshot, query, where } from 'firebase/firestore'
import { getDownloadURL, getStorage, ref, uploadBytes, listAll } from 'firebase/storage';
import firebaseApp from './firebase-config';
import EditProfileBox from './EditProfileBox';

// Connect to current firebase project
const firestore = getFirestore(firebaseApp);
const storage = getStorage(firebaseApp);

// Main function of this page
export default function ProfilePage() {
    const [open, setOpen] = React.useState(false);

    const [users, setUsers] = useState([])
    const [files, setFiles] = useState([])
    const [avatar, setAvatar] = useState([])

    const [relation, setRelation] = useState([])
    const [recommender, setRecommender] = useState([])
    const [graph, setGraph] = useState([])

    /* Identify the current user */
    const user_email = window.localStorage.getItem('user_email');

    /* Firestore SDK queries */
    useEffect(() => {
      const userQuery = query(
        collection(firestore, 'users'),
        where('email', '==', user_email)
      );
        const unsubscribe = onSnapshot(userQuery, snapshot => {
          const user = snapshot.docs.map(doc => doc.data());
          setUsers(user);
          console.log(user[0].firstName)
        })

        return () => {
          unsubscribe()
        }
      }, [])

    /* Storage list functions */
    useEffect(() => {
      listAll(ref(storage, user_email)).then((res) => {
        setFiles(res.items)
      })
    }, [])

    useEffect(() => {
      listAll(ref(storage, user_email+'/Relation Discovery')).then((res) => {
        setRelation(res.items)
      })
    }, [])

    useEffect(() => {
      listAll(ref(storage, user_email+'/Recommender System/')).then((res) => {
        setRecommender(res.items)
      })
    }, [])

    useEffect(() => {
      listAll(ref(storage, user_email+'/Graph Model/')).then((res) => {
        setGraph(res.items)
      })
    }, [])

    /* Show avatar */
    useEffect(() => {
      if (!user_email) {
        setAvatar('https://cdn.icon-icons.com/icons2/1378/PNG/512/avatardefault_92824.png')
      } else {
        const avatarRef = ref(storage, user_email+'/avatar.png')
        getDownloadURL(avatarRef)
        .then((url) => {
          setAvatar(url)
        })
        .catch((error) => {
          switch (error.code) {
            case 'storage/object-not-found':
              setAvatar('https://cdn.icon-icons.com/icons2/1378/PNG/512/avatardefault_92824.png')
              break;

            case 'storage/unknown':
              console.log("Unknown error!")
              break;
          }})
      }
    }, [])

    /* Upload new pic to change ones avatar */
    const onAvatarChange = async (e) => {
      const pic = e.target.files[0]
      const picRef = ref(storage, user_email+'/avatar.png')
      await uploadBytes(picRef, pic).then((snapshot) => {
        console.log("Uploaded Avatar!")
      })
      alert("Upload successfully!")
      const avatarRef = ref(storage, user_email+'/avatar.png')
      getDownloadURL(avatarRef)
      .then((url) => {
        setAvatar(url)
      })
    }

    const navigate = useNavigate()

    /* Redirect to Onboard page to modify the profile data */
    const handleRedirect = (e) => {
      e.preventDefault()
      alert("Now we will go back to onboarding process to re-set your data.")
      navigate("/Onboard")
    }

    const handleEditProfile = (e) => {
        setOpen(true)
    };

    return (
        <Box sx={{ display: 'flex', height: '100%' }}>

            {/* Main space of page*/}
            <Box>
                {/* Title */}
                <Box sx={{ width: '100%' }}>
                    <Typography
                        component="h1"
                        variant="h4"
                        color="inherit"
                        noWrap
                        sx={{ flexGrow: 1, ml: 8, mb: 2, mt:4 }}
                        >
                        Personal Info
                    </Typography>
                </Box>
                
                {/* User profile part */}
                <Box sx={{ mt: 3, ml: 8 }}>
                  <Paper sx={{ display: 'flex', minWidth: 800, minHeight: 60 }}>
                      <Typography
                          component="h1"
                          variant="subtitle1"
                          color="inherit"
                          noWrap
                          sx={{ ml: 8, mt: 2 }}
                        >
                          Avatar: 
                      </Typography>
                      
                      <Box sx={{ ml: 2, mt: 1.5 }}>
                        <Avatar src={avatar} alt='avatar'></Avatar>
                      </Box>

                      <Box sx={{ ml: 6, mt: 1.5 }}>
                        <Button variant="contained" color='primary' component="label">
                          new
                          <input
                            type="file"
                            accept=".png"
                            hidden
                            onChange={onAvatarChange}
                          />
                        </Button>
                      </Box>

                      <Box sx={{ mt: 1.5, ml: 15 }}>
                        <Button variant="contained" color='primary' onClick={handleEditProfile}>Edit profile data</Button>
                      </Box>
                  </Paper>

                  {users.length > 0 &&
                    <EditProfileBox open={open} setOpen={setOpen} user={users[0]}/>
                  }

                  {users?.map((row) => (
                    <Paper sx={{ display: 'flex', minWidth: 800, minHeight: 60, mt: 3 }}>
                        <Typography
                          component="h1"
                          variant="subtitle1"
                          color="inherit"
                          noWrap
                          sx={{ ml: 8, mt: 2 }}
                        >
                          Email: {row.email}
                        </Typography>

                        <Typography
                          component="h1"
                          variant="subtitle1"
                          color="inherit"
                          noWrap
                          sx={{ ml: 8, mt: 2 }}
                        >
                          Phone: {row.phoneNumber}
                        </Typography>
                        <Typography
                          component="h1"
                          variant="subtitle1"
                          color="inherit"
                          noWrap
                          sx={{ ml: 8, mt: 2 }}
                        >
                          Subscription Plan: {row.subscriptionPlan}
                        </Typography>
                    </Paper>
                  ))}

                  {users?.map((row) => (
                    <Paper sx={{ display: 'flex', minWidth: 800, minHeight: 60, mt: 3 }}>
                        <Typography
                          component="h1"
                          variant="subtitle1"
                          color="inherit"
                          noWrap
                          sx={{ ml: 8, mt: 2 }}
                        >
                          First name: {row.firstName}
                        </Typography>

                        <Typography
                          component="h1"
                          variant="subtitle1"
                          color="inherit"
                          noWrap
                          sx={{ ml: 8, mt: 2 }}
                        >
                          Last name: {row.lastName}
                        </Typography>

                        <Typography
                          component="h1"
                          variant="subtitle1"
                          color="inherit"
                          noWrap
                          sx={{ ml: 8, mt: 2 }}
                        >
                          Location: {row.location}
                        </Typography>
                    </Paper>
                  ))}

                  {users?.map((row) => (
                    <Paper sx={{ display: 'flex', minWidth: 800, minHeight: 60, mt: 3 }}>
                        <Typography
                          component="h1"
                          variant="subtitle1"
                          color="inherit"
                          noWrap
                          sx={{ ml: 8, mt: 2 }}
                        >
                          Industry: {row.industry}
                        </Typography>
                        <Typography
                          component="h1"
                          variant="subtitle1"
                          color="inherit"
                          noWrap
                          sx={{ ml: 8, mt: 2 }}
                        >
                          Role: {row.role}
                        </Typography>
                        <Typography
                          component="h1"
                          variant="subtitle1"
                          color="inherit"
                          noWrap
                          sx={{ ml: 8, mt: 2 }}
                        >
                          Goal: {row.goal}
                        </Typography>
                    </Paper>
                  ))}

                    {/* List files from Storage */}
                    <Paper sx={{ display: 'flex', minWidth: 800, minHeight: 60, mt: 3 }}>
                      <Typography
                          component="h1"
                          variant="subtitle1"
                          color="inherit"
                          noWrap
                          sx={{ ml: 8, mt: 2 }}
                        >
                          Your file uploaded in database: 
                      </Typography>
                      <List sx={{ ml: 4, mt: 1 }}>
                        {files?.map((row) => (
                          <ListItemText>{row.name}</ListItemText>
                        ))}
                      </List>
                      <List sx={{ ml: 4, mt: 1 }}>
                        {relation?.map((row) => (
                          <ListItemText>{row.name}</ListItemText>
                        ))}
                      </List>
                      <List sx={{ ml: 4, mt: 1 }}>
                        {recommender?.map((row) => (
                          <ListItemText>{row.name}</ListItemText>
                        ))}
                      </List>
                      <List sx={{ ml: 4, mt: 1 }}>
                        {graph?.map((row) => (
                          <ListItemText>{row.name}</ListItemText>
                        ))}
                      </List>
                    </Paper>
                </Box>

              </Box>

        </Box>
    );
}
</file>

<file path="src/ProfileSettingPage.js">
import { styled } from '@mui/material/styles';
import MuiDrawer from '@mui/material/Drawer';
import * as React from 'react';
import { useState } from "react";
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import IconButton from '@mui/material/IconButton';
import KeyboardDoubleArrowLeftIcon from '@mui/icons-material/KeyboardDoubleArrowLeft';
import KeyboardDoubleArrowRightIcon from '@mui/icons-material/KeyboardDoubleArrowRight';
import Divider from '@mui/material/Divider';
import List from '@mui/material/List';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import AssignmentIcon from '@mui/icons-material/Assignment';
import Button from '@mui/material/Button';
import ButtonBase from '@mui/material/ButtonBase';
import Typography from '@mui/material/Typography';
import { initializeApp } from 'firebase/app';
import { getFirestore, doc, deleteDoc, collection, query, where, onSnapshot } from 'firebase/firestore'
import { getStorage, ref, deleteObject, listAll } from "firebase/storage";
import { getAuth, deleteUser, updateEmail, signOut } from "firebase/auth";
import firebaseApp from './firebase-config';

// Connect to current firebase project
const firestore = getFirestore(firebaseApp);
const storage = getStorage(firebaseApp);

/* Identify the current user */
const user_email = window.localStorage.getItem('user_email');

const Drawer = styled(MuiDrawer, { shouldForwardProp: (prop) => prop !== 'open' })(
    ({ theme, open }) => ({
      '& .MuiDrawer-paper': {
        position: 'relative',
        whiteSpace: 'nowrap',
        width: drawerWidth,
        transition: theme.transitions.create('width', {
          easing: theme.transitions.easing.sharp,
          duration: theme.transitions.duration.enteringScreen,
        }),
        boxSizing: 'border-box',
        ...(!open && {
          overflowX: 'hidden',
          transition: theme.transitions.create('width', {
            easing: theme.transitions.easing.sharp,
            duration: theme.transitions.duration.leavingScreen,
          }),
          width: theme.spacing(7),
          [theme.breakpoints.up('sm')]: {
            width: theme.spacing(9),
          },
        }),
      },
    }),
  );

const drawerWidth = 220;

export default function SettingsPage() {
    const [open, setOpen] = React.useState(false);
    const toggleDrawer = () => {
        setOpen(!open);
    };

    const handleSignOut = () => {
      const auth = getAuth();
      signOut(auth).then(() => {
        console.log("signout")
        window.localStorage.removeItem('access_token');
        window.localStorage.removeItem('industry');
        window.location.reload();
      }).catch((error) => {
        // An error happened.
      });

    }

    const handleDelete = () => {
      if (window.confirm("Do you sure that you want to delete your account? They cannot be recovered once deleted.")) {
        // Delete all recordings in firestore
        const databaseQuery = query(
            collection(firestore, 'userDatabase'),
            where('user_email', '==', user_email)
        );
        onSnapshot(databaseQuery, snapshot => {
            snapshot.docs.map(file => deleteDoc(doc(firestore, "userDatabase", file.id)))
        })

        const modelQuery = query(
            collection(firestore, 'models'),
            where('user_email', '==', user_email)
        );
        onSnapshot(modelQuery, snapshot => {
          snapshot.docs.map(file => deleteDoc(doc(firestore, "models", file.id)))
        })

        const connectorQuery = query(
            collection(firestore, 'connectors'),
            where('user_email', '==', user_email)
        );
        onSnapshot(connectorQuery, snapshot => {
          snapshot.docs.map(file => deleteDoc(doc(firestore, "connectors", file.id)))
        })

        deleteDoc(doc(firestore, "users", user_email))

        // Delete all files in storage
        listAll(ref(storage, user_email)).then((file) => { 
          file.items.forEach(element => {
            deleteObject(ref(storage, user_email+'/'+element.name))
          });
        })

        // Delete user
        const auth = getAuth();
        const user = auth.currentUser;
        deleteUser(user)
        .then(() => {
          window.localStorage.removeItem('access_token');
          window.location.reload();
        }).catch((error) => {
          console.log(error.message)
        })
      } else {
        alert("Canceled!")
      }
    }

    return (
        <Box sx={{ display: 'flex', height: '100%' }}>
            {/* Main space of page*/}
            <Box>
                {/* Title */}
                <Box sx={{ width: '100%' }}>
                    <Typography
                        component="h1"
                        variant="h4"
                        color="inherit"
                        noWrap
                        sx={{ flexGrow: 1, mt:3, ml: 8, mb: 2 }}
                        >
                        Settings
                    </Typography>
                </Box>

                <Box sx={{ ml: 8, mt: 5, display: 'flex' }}>
                  <Typography>Sign Out from this account:</Typography>
                  <Button variant="contained" color="success" sx={{ mt: -0.5, ml: 3 }} onClick={handleSignOut}>Sign Out</Button>
                </Box>

                <Box sx={{ ml: 8, mt: 5, display: 'flex' }}>
                  <Typography>Delete this account:</Typography>
                  <Button variant="contained" color="error" sx={{ mt: -0.5, ml: 3 }} onClick={handleDelete}>Delete</Button>
                </Box>

            </Box>

        </Box>
    );
}
</file>

<file path="src/ServiceRequestPage.js">
import * as React from 'react';
import { useState, useEffect, useCallback } from "react";
import Box from '@mui/material/Box';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import Paper from '@mui/material/Paper';
import Grid from '@mui/material/Grid';
import { getFirestore, doc, deleteDoc, collection, onSnapshot, orderBy, limit, query, where, addDoc, updateDoc } from 'firebase/firestore'
import { getStorage, ref, deleteObject, uploadBytes, getDownloadURL } from "firebase/storage";
import firebaseApp from './firebase-config';
import { styled } from '@mui/material/styles';
import CreateNewRequestPage from './ServiceRequestPageComponents/CreateNewRequestPage';
import MyRequestsPage from './ServiceRequestPageComponents/MyRequestsPage';

// Connect to current firebase project

const firestore = getFirestore(firebaseApp);

export default function ServiceRequestPage() {
  const [value, setValue] = useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  // StyledTab component with custom styles
    const StyledTab = styled(Tab)(({ theme, selected }) => ({
        minWidth: 0, // Allow the tab to shrink
        flex: 1, // Flexible width
        whiteSpace: 'normal', // Allow text to wrap to the next line
        border: '1px solid #CCCCCC', // Border style
        backgroundColor: selected ? '#CCCCCC' : 'inherit', // Grey background when selected
        color: selected ? '#000000' : '#000000', // Black text when selected
        '&:hover': {
          backgroundColor: '#CCCCCC', // Grey background on hover
        },
        fontWeight: 'bold', // Bold text
    }));

      // Function to render content based on the selected tab
    const renderTabContent = (tabIndex) => {
        switch (tabIndex) {
        case 0:
            return <CreateNewRequestPage />;
        case 1:
            return <MyRequestsPage/>
        default:
            return null;
        }
    };

  return (
    <Container maxWidth="lg" sx={{ mt: 2, ml:3, mr:5, mb: 4 }}>
    <Box sx={{ width: '100%' }}>
      <Tabs 
        value={value} 
        onChange={handleChange} 
        aria-label="Finance Menu"
      >
        <StyledTab label="Create New Request" />
        <StyledTab label="My Requests" />
      </Tabs>
      <Paper sx={{ display: 'flex', width: '100%', height: '100%',  mb: 2 }}>
       {/* Render content based on the selected tab */}
       {renderTabContent(value)}
      </Paper>
      
    </Box>
    </Container>
  );
};
</file>

<file path="src/ServiceRequestPageComponents/AddData.js">
import * as React from 'react';
import { useState, useEffect, useCallback } from "react";
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Paper from '@mui/material/Paper';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import LinearProgress from '@mui/material/LinearProgress';
import { Select, Menu, MenuItem, FormControl, InputLabel, Chip, Checkbox , IconButton} from '@mui/material';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogContentText from '@mui/material/DialogContentText';
import DialogTitle from '@mui/material/DialogTitle';
import ButtonBase from '@mui/material/ButtonBase';
import { useDropzone } from "react-dropzone";
import emailjs from "emailjs-com";
import { getFirestore, doc, collection, onSnapshot, orderBy, limit, query, where, addDoc } from 'firebase/firestore'
import { getStorage, ref, uploadBytes, } from "firebase/storage";
import firebaseApp from '../firebase-config';

// Connect to current firebase project
const firestore = getFirestore(firebaseApp);
const storage = getStorage(firebaseApp);


export default function AddData({ selectedItem, open, setOpen, setDataSet, setDataSetId, isFromServiceRequest, serviceRequestId, models}) {

    useEffect(() => {
        const idQuery = query(
            collection(firestore, 'datasources'),
            where('user_email', '==', user_email),
            limit(1),
            orderBy('id', 'desc')
        );
        console.log(idQuery)
        onSnapshot(idQuery, snapshot => {
            console.log("begin id query")
            const t = (snapshot.docs.map(doc => ({ id: doc.data().id })))
            if (!t[0]) {
                setID('0')
                
            } else {
                setID(JSON.stringify(t[0].id))
                console.log("Hi")
            }
        })
    }, [])

   
    const metrics = selectedItem.name
    const user_email = window.localStorage.getItem('user_email');
    const [inputFlow2, setInputFlow2] = useState(false)
    const [filename, setFilename] = useState([])
    const [source, setSource] = useState({"name": ""})
    const [fullHeader, setFullHeader] = useState([])
    const [tmpheader, setTmpheader] = useState([])
    const [tmpdata, setTmpdata] = useState([])
    const [showData, setShowData] = useState(false)
    const [ID, setID] = useState("");
    const [name, setName] = useState([])
    const [type, setType] = useState([])
    const [feedCreate, setFeedCreate] = useState(false)
    const [feedView, setFeedView] = useState(false)
    const [feedData, setFeedData] = useState([]);
    const [dataCategory, setDataCategory] = useState('');
    const [dataOption, setDataOption] = useState('');
    const [addDataConfirmationFlow, setAddDataConfirmationFlow] = useState(false);

    const dataTypeOptions = ['CSV', 'API'];
    const dataOptions = ['Financial Data', 'Sensor Data'];

    const handleClose1 = () => {
        setOpen(false)
    }


    const handleClose2 = () => {
        setInputFlow2(false)
    }

    const handleClose3 = () => {
        setAddDataConfirmationFlow(false)
    }

    const handleHistorical = () => {
        
        setInputFlow2(true)
        setOpen(false)
    }

    const closeCreate = () => {
        setFeedCreate(false)
        setName([]);
        setType([]);
    }

    const closeData = () => {
        setShowData(false)
        setFeedCreate(true)
    }

    const closeView = () => {
        setFeedView(false)
    }

    function formatDate() {
        var d = new Date(),
            month = '' + (d.getMonth() + 1),
            day = '' + d.getDate(),
            year = d.getFullYear();
    
        if (month.length < 2) 
            month = '0' + month;
        if (day.length < 2) 
            day = '0' + day;
    
        return [year, month, day].join('-');
    }

    /* Drag and Drop area */
    const onDrop = useCallback((acceptedFiles) => {
        acceptedFiles.map((file) => {
            uploadFiles(file, file.name, "File uploaded")
        });
    }, []);
    const { getRootProps, getInputProps, acceptedFiles, isDragActive } = useDropzone({ onDrop, accept: {'text/csv': ['.csv']} })

    /* Storage upload functions */
    function uploadFiles(file, name, method) {
        console.log(file)
        setFilename(name)
        setSource({"name": name, "method": method})
        const reader = new FileReader()
  
        reader.onload = function (e) {
          const text = e.target.result;
          const Data = csvToArray(text);
          setTmpdata(Data)
        };
        reader.readAsText(file)
        
        const userRef = ref(storage, user_email+'/'+name)
        uploadBytes(userRef, file).then((snapshot) => {
            console.log("Uploaded file!")
            alert("Upload successfully!")
            handleClose2()
            
            setShowData(true)

            emailjs.send("teamService","template_cqyfsfh",{
                subject: "User uploaded a new file!",
                name: "File name is " + name,
                email: "from " + user_email,
                message: "Please check in the firebase storage",
            }, "r87tnpnYE2FXwhAzx");

            const email = user_email
            const content = "Uploaded a file : " + name
            const date = formatDate()
            const time = new Date()
            addDoc(collection(firestore, 'alerts'), {email, content, date, time})
        })
    }

    function csvToArray(str, delimiter = ",") {
        const headers = str.slice(0, str.indexOf("\n")).split(delimiter);
        setFullHeader(headers)
        console.log(fullHeader)
        if (headers.length > 10) {
          const res = headers.slice(0, 10)
          setTmpheader(res)
        } else {
          setTmpheader(headers)
        }
        const rows = str.slice(str.indexOf("\n") + 1).split("\n");
        const arr = rows.map(function (row) {
          const values = row.split(delimiter);
          const el = headers.reduce(function (object, header, index) {
            object[header] = values[index];
            return object;
          }, {});
          return el;
        });
  
        if (arr.length > 100) {
          return arr.slice(0, 100)
        } else {
          return arr
        }
        return 
    }

    function handleFeedCreate(e) {
        e.preventDefault()
        if (name == "" || type == "") {
            alert("Please give all the information required below!")
            return 
        }

        const CollectionRef = collection(firestore, 'datasources')
        const dataEdit = new Date()
        const id = Number(ID) + 1
        setDataSetId(id)
        console.log("This is updated ID")
        console.log(ID)
        const dataType = type
        const status = "Under Development"
        var file = ''
        var method = ''
        var url = ''
        if (source.name=="") {
            file = 'Under development..'
            setDataSet(file)
            method = 'API connection'
            
        } else {
            file = source.name
            setDataSet(file)
            method = source.method
        }
    
        addDoc(CollectionRef, {id, name, dataEdit, dataType, dataCategory, dataOption, status, siteId: "", user_email, 
        file, method, models, metrics, isFromServiceRequest, url, serviceRequestId})
        .then(response => {
            console.log(response.id)
            const fileId = response.id
        })
        .catch(error => {
            console.log(error.message)
            alert(error.message)
        })

        const email = user_email
        const content = "Created a new feed : " + name
        const date = formatDate()
        const time = new Date()
        addDoc(collection(firestore, 'alerts'), {email, content, date, time})
        closeCreate()
        setAddDataConfirmationFlow(true)
    }

    return (
    <>
    <Dialog open={open} onClose={handleClose1} maxWidth={"sm"} fullWidth={true}>
    <DialogTitle>STEP 1</DialogTitle>
    <DialogContent>
        <DialogContentText>
            Select your data source:
        </DialogContentText>
        
        <Box sx={{ display: 'flex', minHeight: 200, mt: 3, p: 2 }}>
            <ButtonBase sx={{ minWidth: '100%' }} onClick={handleHistorical}>
                <Box display="flex" justifyContent="center" alignItems="center">
                    Historical File
                </Box>
            </ButtonBase>
        </Box>
    </DialogContent>

    <DialogActions>
        <Button onClick={handleClose1}>Cancel</Button>
    </DialogActions>
    </Dialog>

    <Dialog open={inputFlow2} onClose={handleClose2} maxWidth={"md"} fullWidth={true}>
    <DialogTitle>STEP 2</DialogTitle>
    <DialogContent>
        <DialogContentText>
            Please upload your file here
        </DialogContentText>
        
        <Box sx={{ mt: 2 }}>
            <Box sx={{ border: 2, borderStyle: 'dotted' }}>
                <Box {...getRootProps({})} display="flex" justifyContent="center" alignItems="center" sx={{ minHeight: 400 }}>
                    <input {...getInputProps()} onDrop={onDrop}/>
                    {isDragActive ? (
                        <Typography variant="h5">Drop (only .csv file)</Typography>
                    ) : (
                        <Typography variant="h5">Drag file and drop here / Click to upload</Typography>
                    )}
                </Box>
            </Box>
        </Box>
    </DialogContent>

    <DialogActions>
        <Button onClick={handleClose2}>Cancel</Button>
    </DialogActions>
    </Dialog>

    <Dialog open={showData} maxWidth={"lg"} fullWidth={true}>
    <DialogTitle>Data Check</DialogTitle>
    <DialogContent>
        <DialogContentText>
            Can check part content of your file below
        </DialogContentText>
        
        <Box>
            <TableContainer component={Paper} sx={{ mt: 2 }}>
                <Table
                sx={{ minWidth: 650 }}
                size="small"
                aria-label="a dense table"
                >
                <TableHead>
                    <TableRow>
                    {tmpheader?.map((column) => (
                        <TableCell align="right">{column}</TableCell>
                    ))}
                    </TableRow>
                </TableHead>

                <TableBody>
                    {tmpdata?.map((row) => (
                    <TableRow
                        key={Object.values(row)[0]}
                        sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
                    >
                        <TableCell component="th" scope="row">
                        {Object.values(row)[0]}
                        </TableCell>
                        <TableCell align="right">{Object.values(row)[1]}</TableCell>
                        <TableCell align="right">{Object.values(row)[2]}</TableCell>
                        <TableCell align="right">{Object.values(row)[3]}</TableCell>
                        <TableCell align="right">{Object.values(row)[4]}</TableCell>
                        <TableCell align="right">{Object.values(row)[5]}</TableCell>
                        <TableCell align="right">{Object.values(row)[6]}</TableCell>
                        <TableCell align="right">{Object.values(row)[7]}</TableCell>
                        <TableCell align="right">{Object.values(row)[8]}</TableCell>
                        <TableCell align="right">{Object.values(row)[9]}</TableCell>
                    </TableRow>
                    ))}
                </TableBody>
                </Table>
            </TableContainer>
        </Box>
    </DialogContent>

    <DialogActions>
        <Button onClick={closeData}>Set up Feed</Button>
    </DialogActions>
    </Dialog>

    <Dialog open={feedView} onClose={closeView} maxWidth={"lg"} fullWidth={true}>
    <DialogTitle>Information View</DialogTitle>
    <DialogContent>
        <Box>
            <FormControl sx={{ ml: 2 }}>
                {feedData?.map((row) => (
                <div>
                    <Typography variant="h7">Basic Info</Typography>
                    <Box sx={{ mt: 1 }}>
                        <TextField label="No." variant="standard" InputProps={{ readOnly: true }} defaultValue={row.id} />
                        <TextField label="Name" variant="standard" InputProps={{ readOnly: true }} defaultValue={row.name} sx={{ ml: 4 }}/>
                        <TextField label="Type" variant="standard" InputProps={{ readOnly: true }} defaultValue={row.dataType} sx={{ ml: 4 }}/>
                        <TextField label="Creation Time" variant="standard" InputProps={{ readOnly: true }} defaultValue={new Date(row.dataEdit * 1000)} sx={{ ml: 4 }}/>
                        <TextField label="Creation Method" variant="standard" InputProps={{ readOnly: true }} defaultValue={row.method} sx={{ ml: 4 }}/>
                    </Box>

                    <Box sx={{ mt: 2 }}>
                        <Typography variant="h7" >Status: {row.status}</Typography>
                        <Box sx={{ mt: 2 }}>
                            <LinearProgress variant="determinate" value={parseInt(row.status.substr(0, row.status.length - 1))} />
                        </Box>
                    </Box>


                    <Box sx={{ mt: 2 }}>
                        <Typography variant="h7">Models attached: {row.models}</Typography>
                    </Box>

                    <Box sx={{ mt: 2}}>
                    <Typography variant="h7">File:</Typography>
                        <TableContainer component={Paper} sx={{ mt: 1 }}>
                            <Table
                            sx={{ width: '100%' }}
                            size="small"
                            aria-label="a dense table"
                            >
                            <TableHead>
                                <TableRow>
                                {tmpheader.slice(0, 5)?.map((column) => (
                                    <TableCell align="right">{column}</TableCell>
                                ))}
                                </TableRow>
                            </TableHead>

                            <TableBody>
                                {tmpdata.slice(0, 5)?.map((row) => (
                                <TableRow
                                    key={Object.values(row)[0]}
                                    sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
                                >
                                    <TableCell component="th" scope="row">
                                    {Object.values(row)[0]}
                                    </TableCell>
                                    <TableCell align="right">{Object.values(row)[1]}</TableCell>
                                    <TableCell align="right">{Object.values(row)[2]}</TableCell>
                                    <TableCell align="right">{Object.values(row)[3]}</TableCell>
                                    <TableCell align="right">{Object.values(row)[4]}</TableCell>
                                </TableRow>
                                ))}
                            </TableBody>
                            </Table>
                        </TableContainer>
                    </Box>
                    </div>
                ))}
            </FormControl>
        </Box>
        </DialogContent>

    <DialogActions>
        <Button onClick={closeView}>Close</Button>
    </DialogActions>
    </Dialog>


    <Dialog open={feedCreate} onClose={closeCreate}>
    <DialogTitle>Custom Data</DialogTitle>
    <DialogContent>
        <DialogContentText>
            Please fill in these fields to label your data.
        </DialogContentText>

        <FormControl sx={{ mt: 2, mb: 2, minWidth: 500 }}>
            <TextField autoFocus margin="dense" id="name" label="Name this feed" fullWidth variant="standard" onChange={(e) => {setName(e.target.value)}} />
            <FormControl variant="outlined" sx={{ mt: 2, minWidth: 300 }}>
                <InputLabel>Data Type</InputLabel>
                <Select
                value={type}
                onChange={(e) => {setType(e.target.value)}}
                label="Select Data Type"
                >
                {dataTypeOptions.map((option) => (
                    <MenuItem key={option} value={option}>
                    {option}
                    </MenuItem>
                ))}
                </Select>
            </FormControl>
        </FormControl>

        <FormControl sx={{ mt: 2, mb: 2, minWidth: 500 }}>
            <FormControl variant="outlined" sx={{ mt: 2, minWidth: 300 }}>
                <InputLabel>Data Options</InputLabel>
                <Select
                value={dataOption}
                onChange={(e) => {setDataOption(e.target.value)}}
                label="Select Data Option"
                >
                {dataOptions.map((option) => (
                    <MenuItem key={option} value={option}>
                    {option}
                    </MenuItem>
                ))}
                </Select>
            </FormControl>
        </FormControl>

        {dataOption == 'Financial Data' &&
        <FormControl sx={{ mt: 2, mb: 2, minWidth: 500 }}>
            <FormControl variant="outlined" sx={{ mt: 2, minWidth: 300 }}>
                <InputLabel>Data Category</InputLabel>
                <Select
                value={dataCategory}
                onChange={(e) => {setDataCategory(e.target.value)}}
                label="Select Data Category"
                >
                {selectedItem.datasource.map((option) => (
                    <MenuItem key={option} value={option}>
                    {option}
                    </MenuItem>
                ))}
                </Select>
            </FormControl>
        </FormControl>
        }

        {dataOption == "Sensor Data" &&
            <FormControl sx={{ mt: 2, mb: 2, minWidth: 500 }}>
                <FormControl variant="outlined" sx={{ mt: 2, minWidth: 300 }}>
                    <InputLabel>Sensor Data Category</InputLabel>
                    <Select
                    value={dataCategory}
                    onChange={(e) => {setDataCategory(e.target.value)}}
                    label="Select Data Category"
                    >
                    {selectedItem.sensorFieldData.map((option) => (
                        <MenuItem key={option} value={option}>
                        {option}
                        </MenuItem>
                    ))}
                    </Select>
                </FormControl>
            </FormControl>
        }
    </DialogContent>

    <DialogActions>
        <Button onClick={closeCreate}>Cancel</Button>
        <Button onClick={handleFeedCreate}>Create</Button>
    </DialogActions>
    </Dialog>
    <Dialog open={addDataConfirmationFlow} onClose={handleClose2} maxWidth={"sm"} fullWidth={true}>
            <DialogTitle>Successfully set the data!</DialogTitle>
            <DialogActions>
                <Button onClick={handleClose3}>OK</Button>
            </DialogActions>
    </Dialog>
</>
    )

}
</file>

<file path="src/ServiceRequestPageComponents/CreateNewRequestPage.js">
import * as React from 'react';
import { useState, useEffect } from "react";
import Box from '@mui/material/Box';
import {Typography, ListItem, Paper, Grid, Button, Dialog, DialogActions, 
        DialogContent, DialogContentText, DialogTitle, ButtonBase, Select,
        MenuItem, FormControl, InputLabel, Stack, TextField
        } from '@mui/material';
        import { getFirestore, doc, deleteDoc, collection, onSnapshot, orderBy, limit, query, where, addDoc, updateDoc } from 'firebase/firestore'
import firebaseApp from '../firebase-config';
import AddData from './AddData.js'

// Connect to current firebase project
const firestore = getFirestore(firebaseApp);

export default function CreateNewRequestPage() {
    const user_email = window.localStorage.getItem('user_email');
    const industry = window.localStorage.getItem('industry');
    const [srTypes, setSRTypes] = useState([]);
    const [inputFlow1, setInputFlow1] = useState(false);
    const [confirmationFlow, setConfirmationFlow] = useState(false);
    const [modelType, setModelType] = useState('');
    const [requestType, setRequestType] = useState('');
    const [metricsList, setMetricsList] = useState('');
    const [metrics, setMetrics] = useState('');
    const [viewGroup, setViewGroup] = useState('');
    const [requestGroup, setRequestGroup] = useState('');
    const [useGroup, setUseGroup] = useState('');
    const [additionalInfo, setAdditionalInfo] = useState('');
    const [timeFrameDate, setTimeFrameDate] = useState('');
    const [dataUploadStatus, setDataUploadStatus] = useState('');
    const [open, setOpen] = useState(false);
    const [selectedItem, setSelectedItem] = useState({});
    const [priority, setPriority] = useState('');
    const [dataset, setDataSet] = useState('');
    const [datasetId, setDataSetId] = useState('');
    const [serviceRequestId, setServiceRequestId] = useState('');

    const priorityOptions = ['High', 'Medium', 'Low']
    
    
     /* Firestore SDK queries */
     React.useEffect(() => {
        console.log(industry)
        const metricsQuery = query(
            collection(firestore, 'metrics'),
            where('industry', '==', industry),
            orderBy('id')
            );

        onSnapshot(metricsQuery, snapshot => {
            const metrics = snapshot.docs.map(doc => ({id: doc.id, data: doc.data() }))
            setMetricsList(metrics)
        })
        
    }, []);

    useEffect(() => {
        const srTypeQuery = query(
        collection(firestore, 'serviceRequests'),
        orderBy('id')
        );
        const unsubscribe = onSnapshot(srTypeQuery, snapshot => {
            setSRTypes(snapshot.docs.map(doc => ({id: doc.id, data: doc.data() })))
        })
    
        return () => {
            unsubscribe()
        }
        }, [])

    function handleRequest(type) {
        setInputFlow1(true)
        setRequestType(type)
        setServiceRequestId(generateRandomId(20))
    };

    const handleMetricChange = (e) => {
        setMetrics(e.target.value)
    };

    const handleItemClick = (item) => {
        setSelectedItem(item);
      };


    function handleAdd() { 
        setOpen(true)
    }
    const handleClose1 = () => {
        setInputFlow1(false)
    }

    const handleTextChange = (e) => {
        setAdditionalInfo(e.target.value)
    }

    const handleSubmit = (e) => {
       
    }

    const handleClose2 = () => {
        setConfirmationFlow(false)
    }

    const getTimeFrameDate = (days) => {
        const currentDate = new Date();
        const futureDate = new Date();
        futureDate.setDate(currentDate.getDate() + days);
        const formattedDate = futureDate.toLocaleDateString("en-US", {
            day: "numeric",
            month: "long",
            year: "numeric"
          });
         return formattedDate;
    };

    const handleModelSelection = (model) => {
        setModelType(model);
        setTimeFrameDate(getTimeFrameDate(7));
    }


    const generateRandomId = (length) => {
        let result = '';
        const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        const charactersLength = characters.length;
        
        for (let i = 0; i < length; i++) {
            result += characters.charAt(Math.floor(Math.random() * charactersLength));
        }
        
        return result;
        };

    function handleRequestCreate(e) {
       
        e.preventDefault()
        if (modelType == "" || metrics == "" || viewGroup == "" || requestGroup == "" || useGroup == "" || priority == "") {
            alert("Please give all the information required below!")
            return 
        }
        setInputFlow1(false)
        setConfirmationFlow(true)
        const CollectionRef = collection(firestore, 'userServiceRequests')
        const requestTime = new Date()
        const requestDate = requestTime.toLocaleDateString("en-US", {
            day: "numeric",
            month: "long",
            year: "numeric"
            });
        
        const id = serviceRequestId
        const timeToDevelop = 7
        const operator = "OP"
        const status = "Under Development"

        const model = modelType
        

        addDoc(CollectionRef, {id, industry, requestType, model, dataset, datasetId, timeToDevelop, metrics, operator, status, requestDate, requestTime, user_email, })
        .then(response => {
            console.log(response.id)
            const fileId = response.id
            console.log("Request created successfully! Please check it on <My Request> page.")
        })
        .catch(error => {
            console.log(error.message)
            alert(error.message)
        })

        const email = user_email
        const content = "Created a new request : " + model
        const date = requestDate
        const time = new Date()
        addDoc(collection(firestore, 'alerts'), {email, content, date, time})
    }

    return (
         
        <Box sx={{ flexGrow: 1, maxWidth: 1504, bgcolor: '#FAFAFA'}}>
            <ListItem>
                <Typography
                    component="h1"
                    variant="h6"
                    color="inherit"
                    noWrap
                    sx={{ flexGrow: 1,fontWeight: 'bold', mt:2, ml:2, mr: 3 }}
                >
                    Request Type
                </Typography>
            </ListItem>
            <Grid container sx={{mt:4}}>
                {srTypes.map((item,index) => (
                    <Grid item xs={6} key={index} >
                        <Paper
                        sx={{
                            p: 0.5,
                            display: 'flex',
                            flexDirection: 'column',
                            height: 200,
                            mt:2,
                            ml:4,
                            mr:4
                        }}
                        >
                        <Typography
                            component="h1"
                            variant="h6"
                            color="inherit"
                            
                            sx={{ flexGrow: 1,fontWeight: 'bold', mt:2, ml:2, mr: 3 }}
                        >
                            {item.data.name}
                        </Typography>
                        <Typography
                            component="h1"
                            variant="h7"
                            color="inherit"
                            sx={{ flexGrow: 1, mt:1, ml:2, mr: 3 }}
                        >
                            {item.data.description}
                        </Typography>
                        <Button
                            variant="h8"
                            style={{ alignSelf: 'flex-end', color: '#1976D2' }}
                            onClick={() => handleRequest(item.data.name)}
                        >
                            REQUEST
                        </Button>
                        
                            <Dialog open={inputFlow1} onClose={handleClose1} maxWidth={"sm"} fullWidth={true}>
                                <DialogTitle>New Request</DialogTitle>
                                <DialogContent>
                                <Stack direction="row" spacing={0}>
                                    <Typography
                                    component="h1"
                                    variant="h7"
                                    color="inherit"
                                    sx={{ flexGrow: 1, mt:1, ml:2, mr: 3, mb:2 }}
                                >
                                    Request Type
                                    </Typography>
                                    <Typography
                                    component="h1"
                                    variant="h7"
                                    color="inherit"
                                    sx={{ flexGrow: 1, mt:1, ml:2, mr: 3, mb:2 }}
                                >
                                    {requestType}
                                    </Typography>
                                </Stack>
                                {requestType == "AI Model" &&
                                <Stack direction="row" spacing={0}>
                                    <Typography
                                    component="h1"
                                    variant="h7"
                                    color="inherit"
                                    sx={{ flexGrow: 1, mt:1, ml:2, mr: 3, mb:2 }}
                                >
                                    Type of Models
                                    </Typography>
                                    <TextField variant="standard" defaultValue="" style={{ width: '300px' }} onChange={(e) => {setModelType(e.target.value)}}/>
                                </Stack>
                                }

                                <Stack direction="row" spacing={0}>
                                    <Typography
                                    component="h1"
                                    variant="h7"
                                    color="inherit"
                                    sx={{ flexGrow: 1, mt:1, ml:2, mr: 3 }}
                                >
                                    Metrics
                                    </Typography>
                                    <FormControl variant="outlined" sx={{ mt: 1, minWidth: 300 }}>
                                        <InputLabel>Type of Metrics</InputLabel>
                                        <Select
                                        value={metrics}
                                        onChange={handleMetricChange}
                                        label="Select Metrics"
                                        >
           
                                        {metricsList.map((option) => ( 
                                            <MenuItem 
                                            key={option.data.name} 
                                            value={option.data.name}
                                            onClick={() => handleItemClick(option.data)}
                                            >
                                            {option.data.name}
                                            </MenuItem>
                                        ))}
                                    </Select>
                                    </FormControl>
                                </Stack>

                                <Stack direction="row" spacing={0} >
                                    <Typography
                                    component="h1"
                                    variant="h7"
                                    color="inherit"
                                    sx={{ flexGrow: 1, mt:1, ml:2, mr: 3 }}
                                >
                                    Data Feed
                                    </Typography>
                                    
                                <Button 
                                    variant="h7" 
                                    sx={{ bgcolor: '#DEDEDE', boxShadow: '0px 2px 4px rgba(0, 0, 0, 0.1)', mt:1 }}
                                    onClick={handleAdd}
                                    >
                                        + ADD DATA
                                </Button>
                                {metrics &&
                                <AddData 
                                    selectedItem = {selectedItem}
                                    open={open} setOpen={setOpen}
                                    setDataSet={setDataSet}
                                    setDataSetId={setDataSetId}
                                    isFromServiceRequest = {true}
                                    serviceRequestId = {serviceRequestId}
                                    models = {modelType}
                                ></AddData>
                                }
                                </Stack>

                                <Stack direction="row" spacing={0} >
                                    <Typography
                                    component="h1"
                                    variant="h7"
                                    color="inherit"
                                    sx={{ flexGrow: 1, mt:2, ml:2, mr: 3, mb:2 }}
                                >
                                    Users
                                    </Typography> 
                                </Stack>

                                <Stack direction="row" spacing={0} >
                                <Typography
                                    component="h1"
                                    variant="h7"
                                    color="inherit"
                                    sx={{ flexGrow: 1, mt:1, ml:4, mr: 3 }}
                                >
                                    Who can see the data
                                    </Typography>
                                    <FormControl variant="outlined" sx={{ mt: 1, minWidth: 300 }}>
                                        
                                        <Select
                                        value={viewGroup}
                                        onChange={(e) => {setViewGroup(e.target.value)}}
                                        label="Select Model Type"
                                        >
                                        {/* {selectedItem.datasource.map((option) => ( */}
                                            <MenuItem key="ALL GROUPS" value="ALL GROUPS" >
                                            ALL GROUPS
                                            </MenuItem>
                                        {/* ))} */}
                                    </Select>
                                    </FormControl>
                                </Stack>

                                <Stack direction="row" spacing={0} >
                                <Typography
                                    component="h1"
                                    variant="h7"
                                    color="inherit"
                                    sx={{ flexGrow: 1, mt:1, ml:4, mr: 3 }}
                                >
                                    Who can request the data
                                    </Typography>
                                    <FormControl variant="outlined" sx={{ mt: 1, minWidth: 300 }}>
                                        
                                        <Select
                                        value={requestGroup}
                                        onChange={(e) => {setRequestGroup(e.target.value)}}
                                        label="Select Model Type"
                                        >
                                        {/* {selectedItem.datasource.map((option) => ( */}
                                            <MenuItem key="DATA GROUPS" value="DATA GROUPS" >
                                            DATA GROUPS
                                            </MenuItem>
                                        {/* ))} */}
                                    </Select>
                                    </FormControl>
                                </Stack>
                                <Stack direction="row" spacing={0} >
                                <Typography
                                    component="h1"
                                    variant="h7"
                                    color="inherit"
                                    sx={{ flexGrow: 1, mt:1, ml:4, mr: 3 }}
                                >
                                    Who can use the data
                                    </Typography>
                                    <FormControl variant="outlined" sx={{ mt: 1, minWidth: 300 }}>
                                        
                                        <Select
                                        value={useGroup}
                                        onChange={(e) => {setUseGroup(e.target.value)}}
                                        label="Select Model Type"
                                        >
                                        {/* {selectedItem.datasource.map((option) => ( */}
                                            <MenuItem key="DATA GROUPS" value="DATA GROUPS" >
                                            DATA GROUPS
                                            </MenuItem>
                                        {/* ))} */}
                                    </Select>
                                    </FormControl>
                                </Stack>

                                
                                <Stack direction="row" spacing={0} >
                                <Typography
                                    component="h1"
                                    variant="h7"
                                    color="inherit"
                                    sx={{ flexGrow: 1, mt:1, ml:2, mr: 3 }}
                                >
                                    Priority
                                </Typography>
                                    <FormControl variant="outlined" sx={{ mt: 1, minWidth: 300 }}>
                                        
                                        <Select
                                        value={priority}
                                        onChange={(e) => {setPriority(e.target.value)}}
                                        label="Select Model Type"
                                        >
                                        {priorityOptions.map((option) => (
                                    <MenuItem key={option} value= {option}>
                                            {option}
                                            </MenuItem>
                                         ))} 
                                    </Select>
                                    </FormControl>
                                </Stack>
                                <Typography
                                    component="h1"
                                    variant="h7"
                                    color="inherit"
                                    sx={{ flexGrow: 1, mt:1, ml:2, mr: 3 }}
                                >
                                    Additional Information
                                    </Typography>
                                <TextField
                                variant="outlined"
                                fullWidth
                                multiline
                                rows={2}
                                value={additionalInfo}
                                onChange={handleTextChange}
                                sx={{ flexGrow: 1, mt:2, ml:2, mr: 3 }}
                                />
                                {timeFrameDate &&
                                <Typography
                                    component="h1"
                                    variant="h12"
                                    color="#979797"
                                    sx={{ flexGrow: 1, mt:1, ml:2, mr: 3 }}
                                >
                                    Estimated Timeframe: 7 days, {timeFrameDate}
                                </Typography>
                                }
                                </DialogContent>

                                <DialogActions>
                                <Button onClick={handleRequestCreate}>OK</Button>
                                    <Button onClick={handleClose1}>Cancel</Button>
                                </DialogActions>
                            </Dialog>
                        
                        <Dialog open={confirmationFlow} onClose={handleClose2} maxWidth={"sm"} fullWidth={true}>
                            <DialogTitle>Confirmation</DialogTitle>
                            <DialogContent>

                            <Typography
                                component="h1"
                                variant="h12"
                                color="#979797"
                                sx={{ flexGrow: 1, mt:1, ml:2, mr: 3 }}
                            >
                                {requestType} request successfully submitted!
                            </Typography>
                            </DialogContent>

                            <DialogActions>
                                <Button onClick={handleClose2}>OK</Button>
                            </DialogActions>
                        </Dialog>
        
                    </Paper>

                </Grid>
                
                ))}
            </Grid>
        </Box>
    );
}
</file>

<file path="src/ServiceRequestPageComponents/MyRequestsPage.js">
import * as React from 'react';
import { useState, useEffect } from "react";
import Box from '@mui/material/Box';
import ListItem from '@mui/material/ListItem';
import Typography from '@mui/material/Typography';
import { Table, TableContainer, TableHead, TableRow, TableCell, TableBody, Paper } from '@mui/material';
import firebaseApp from '../firebase-config';
import { getFirestore, collection, onSnapshot, orderBy, query, where, } from 'firebase/firestore'

// Connect to current firebase project
const firestore = getFirestore(firebaseApp);

export default function MyRequestsPage() {

    /* Identify the current user */
    const user_email = window.localStorage.getItem('user_email');
    const [userServiceRequests, setUserServiceRequests] = useState([]);

    /* Firestore SDK queries */
    useEffect(() => {
        const userServiceRequestsQuery = query(
            collection(firestore, 'userServiceRequests'),
            where('user_email', '==', user_email),
            orderBy("requestTime", 'desc')
        );
        const unsubscribe = onSnapshot(userServiceRequestsQuery, snapshot => {
            setUserServiceRequests(snapshot.docs.map(doc => ({id: doc.id, data: doc.data() })));
        })

        return () => {
            unsubscribe()
        }
        }, [])

    return (
            
        <Box sx={{ flexGrow: 1, maxWidth: 1504, bgcolor: '#FAFAFA'}}>
            <ListItem>
                <Typography
                    component="h1"
                    variant="h6"
                    color="inherit"
                    noWrap
                    sx={{ flexGrow: 1,fontWeight: 'bold', mt:2, ml:2, mr: 3 }}
                >
                    My Requests
                </Typography>
                

            </ListItem>
            <TableContainer component={Paper} sx={{ml:4, mr:4, maxWidth: 1090}}>
                <Table>
                    <TableHead>
                    <TableRow>
                        <TableCell>Industry</TableCell>
                        <TableCell>Request</TableCell>
                        <TableCell>Datasets</TableCell>
                        <TableCell>Time to Develop</TableCell>
                        <TableCell>Metric</TableCell>
                        <TableCell>Operator</TableCell>
                        <TableCell>Status</TableCell>
                        <TableCell>Request Date</TableCell>
                    </TableRow>
                    </TableHead>
                    <TableBody>
                    {userServiceRequests.map((item, index) => (
                        <TableRow key={index}>
                        <TableCell>{item.data.industry}</TableCell>
                        <TableCell>{item.data.requestType}</TableCell>
                        <TableCell>{item.data.dataset}</TableCell>
                        <TableCell>{item.data.timeToDevelop} days</TableCell>
                        <TableCell>{item.data.metrics}</TableCell>
                        <TableCell>{item.data.operator}</TableCell>
                        <TableCell>{item.data.status}</TableCell>
                        <TableCell>{item.data.requestDate}</TableCell>
                        </TableRow>
                    ))}
                    </TableBody>
                </Table>
    </TableContainer>
        </Box>
    );
}
</file>

<file path="src/SignInPage.js">
import * as React from "react";
import { useState } from "react";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import Link from "@mui/material/Link";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import emailjs from "emailjs-com";
import { useNavigate } from "react-router-dom";
import [Third party] } from "react";
import { createTheme, ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { getAuth, signInWithEmailAndPassword, sendPasswordResetEmail, signOut, signInWithPopup, GoogleAuthProvider, sendSignInLinkToEmail, isSignInWithEmailLink, signInWithEmailLink, getAdditionalUserInfo } from "firebase/auth";


// Customize the theme/style
const mdTheme = createTheme({
  palette: {
    mode: 'dark',
    background: {
      default: '#031c4a',
      paper: '#031c4a',
    },
    error: {
      main: '#060c43',
    },
    warning: {
      main: '#00e676',
    },
    success: {
      main: '#ffb74d',
    },
  },
});

export default function SignInPage() {
  const navigate = useNavigate();
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");

  useEffect(() => {
  const token =  window.localStorage.getItem('access_token');
  if(token) navigate("/Dashboard/Welcome");
  },[])

  const handleSubmit = (event) => {
    const data = new FormData(event.currentTarget);
    if (!data.get("email") || !data.get("password")) {
      alert("Please enter correct email and password!")
    } else{
        const auth = getAuth();
        signInWithEmailAndPassword(auth, data.get("email"), data.get("password"))
        .then((userCredential) => {
          const user = userCredential.user;
          if (!user.emailVerified) {
            alert("You haven't verified your email address! Please check your email inbox. \nIf you have verified and still get this, please refresh this page!")
            auth.signOut()
          } else {
            setEmail("");
            setPassword("");
            window.localStorage.setItem('access_token', user.refreshToken)
            window.localStorage.setItem('user_email', email)
            window.localStorage.setItem('uid', user.uid)
            console.log(user);
            window.location.reload()
          }
        })
        .catch((error) => {
          // Handle authentication errors
          if (error.code === "auth/wrong-password") {
            alert("Incorrect password")
            console.log("Incorrect password");
          } else if (error.code === "auth/user-not-found") {
            console.log("User not found");
            alert("User not found")
          } else {
            console.log("Error:", error.message);
          }
        });
      }
    event.preventDefault();

    console.log({
      email: data.get("email"),
      password: data.get("password"),
    });
  };

  function SignInGoogle() {
    const auth = getAuth();
    const provider = new GoogleAuthProvider();
    signInWithPopup(auth, provider)
      .then((result) => {
        const user = result.user;
        if (getAdditionalUserInfo(result).isNewUser) {
          emailjs.send("teamService","template_cqyfsfh",{
            subject: "New registered user!",
            email: "The email address of the new user is " + user.email,
            message: "He registered at " + user.metadata.creationTime,
          }, "r87tnpnYE2FXwhAzx")
          emailjs.send("teamService","template_frf9asv",{
            subject: "New registered user!",
            email: "The email address of the new user is " + user.email,
            message: "He registered at " + user.metadata.creationTime,
          }, "r87tnpnYE2FXwhAzx")
          .then(() => {
            window.localStorage.setItem('access_token', result.user.accessToken)
            window.localStorage.setItem('user_email', user.email)
            window.localStorage.setItem('uid', user.uid)
            console.log(result);
            window.location.reload()
          })
        } else {
          window.localStorage.setItem('access_token', result.user.accessToken)
          window.localStorage.setItem('user_email', user.email)
          window.localStorage.setItem('uid', user.uid)
          console.log(result);
          window.location.reload()
        }
      }).catch((error) => {
        console.log(error.message)
        alert(error.message)
      });
  }


  /* User request to change his password */
  const onPasswordChange = () => {
    const auth = getAuth();
    sendPasswordResetEmail(auth, email)
    .then(() => {
      alert("Please check your inbox of current email address!")
      console.log("Send successfully!")
      window.localStorage.clear()
    })
    .catch((error) => {
      const errorCode = error.code;
      const errorMessage = error.message;
      console.log(errorCode, errorMessage)
      alert(errorMessage)
    });
  }

  return (
    <ThemeProvider theme={mdTheme}>
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <Box
        sx={{
          marginTop: 8,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <Avatar sx={{ m: 1, bgcolor: "secondary.main" }}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Sign in
        </Typography>

        {/* Text fields */}
        <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
          <TextField
            margin="normal"
            required
            fullWidth
            id="email"
            label="Email Address"
            name="email"
            autoComplete="email"
            autoFocus
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <TextField
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            autoComplete="current-password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <FormControlLabel
            control={<Checkbox value="remember" color="primary" />}
            label="Remember me"
          />
          <Button
            type="submit"
            fullWidth
            color="secondary"
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
          >
            Sign In
          </Button>
        </Box>

        <Button
            type="submit"
            fullWidth
            variant="contained"
            sx={{ mt: 1, mb: 1 }}
            style={{
              backgroundColor: "#FFFAFA",
            }}
            onClick={SignInGoogle}
          >
            Sign In with Google
          </Button>

          <Grid container>
            <Grid item>
              <Link href="SignUp" variant="body2">
                {"Don't have an account? Sign Up"}
              </Link>
            </Grid>
            <Grid item sx={{ ml: 9.5 }}>
              <Link onClick={onPasswordChange} variant="body2">
                {"Forget password?"}
              </Link>
            </Grid>
          </Grid>
      </Box>
    </Container>
    </ThemeProvider>
  );
}
</file>

<file path="src/SignUpPage.js">
import * as React from "react";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import TextField from "@mui/material/TextField";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import Link from "@mui/material/Link";
import Grid from "@mui/material/Grid";
import Box from "@mui/material/Box";
import LockOutlinedIcon from "@mui/icons-material/LockOutlined";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import { createTheme, ThemeProvider } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import emailjs from "emailjs-com";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { getAuth, createUserWithEmailAndPassword, sendEmailVerification, signOut, signInWithPopup, GoogleAuthProvider, sendSignInLinkToEmail, getAdditionalUserInfo } from "firebase/auth";

// Customize the theme/style
const mdTheme = createTheme({
  palette: {
    mode: 'dark',
    background: {
      default: '#031c4a',
      paper: '#031c4a',
    },
    error: {
      main: '#060c43',
    },
    warning: {
      main: '#00e676',
    },
    success: {
      main: '#ffb74d',
    },
  },
});

export default function SignUpPage() {
 const navigate = useNavigate();
 const [email,setEmail] = useState();
 const [password,setPassword] = useState();

  // SDK way to sign up (new)
  const handleSubmit = (event) => {
    const data = new FormData(event.currentTarget);
    if (!data.get("email") || !data.get("password")) {
      alert("Please enter correct email and password!")
    } else {
      if (data.get("password").length < 8) {
        alert("The password is too short! Please enter a password that has more than 8 characters.")
      }
      else {
        const auth = getAuth();
        createUserWithEmailAndPassword(auth, data.get("email"), data.get("password"))
          .then((userCredential) => {
            const user = userCredential.user;
            emailjs.send("teamService","template_cqyfsfh",{
              subject: "New registered user!",
              email: "The email address of the new user is " + user.email,
              message: "He registered at " + user.metadata.creationTime,
            }, "r87tnpnYE2FXwhAzx");
            emailjs.send("teamService","template_frf9asv",{
              subject: "New registered user!",
              email: "The email address of the new user is " + user.email,
              message: "He registered at " + user.metadata.creationTime,
            }, "r87tnpnYE2FXwhAzx");
            
            sendEmailVerification(user)
            .then(() => {
              alert("Successful! Please check your email and verify the address by link before sign in.")
              auth.signOut()
              navigate('/')
            })
          })
          .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            alert(errorMessage)
          });
      }
    }
    event.preventDefault();
  }

  useEffect(() => {
    const token =  window.localStorage.getItem('access_token');
    if(token) navigate("/Dashboard/Welcome");
    },[])

  function SignInGoogle() {
    const auth = getAuth();
    const provider = new GoogleAuthProvider();
    signInWithPopup(auth, provider)
      .then((result) => {
        const user = result.user;
        if (getAdditionalUserInfo(result).isNewUser) {
          emailjs.send("teamService","template_cqyfsfh",{
            subject: "New registered user!",
            email: "The email address of the new user is " + user.email,
            message: "He registered at " + user.metadata.creationTime,
          }, "r87tnpnYE2FXwhAzx")
          emailjs.send("teamService","template_frf9asv",{
            subject: "New registered user!",
            email: "The email address of the new user is " + user.email,
            message: "He registered at " + user.metadata.creationTime,
          }, "r87tnpnYE2FXwhAzx")
          .then(() => {
            window.localStorage.setItem('access_token', result.user.accessToken)
            window.localStorage.setItem('user_email', user.email)
            window.localStorage.setItem('uid', user.uid)
            console.log(result);
            window.location.reload()
          })
        } else {
          window.localStorage.setItem('access_token', result.user.accessToken)
          window.localStorage.setItem('user_email', user.email)
          window.localStorage.setItem('uid', user.uid)
          console.log(result);
          window.location.reload()
        }
        
      }).catch((error) => {
        console.log(error.message)
        alert(error.message)
      });
  }

  return (
    <ThemeProvider theme={mdTheme}>
    <Container component="main" maxWidth="xs">
      <CssBaseline />
      <Box
        sx={{
          marginTop: 8,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <Avatar sx={{ m: 1, bgcolor: "primary.main" }}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component="h1" variant="h5">
          Sign up
        </Typography>

        {/* Text fields */}
        <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
          <TextField
            onChange ={(e) => setEmail(e.target.value)}
            value={email}
            margin="normal"
            required
            fullWidth
            id="email"
            label="Email Address"
            name="email"
            autoComplete="email"
            autoFocus
          />
          <TextField
            onChange ={(e) => setPassword(e.target.value)}
           value={password}
            margin="normal"
            required
            fullWidth
            name="password"
            label="Password"
            type="password"
            id="password"
            autoComplete="current-password"
          />
          <FormControlLabel
            control={<Checkbox value="remember" color="primary" />}
            label="Remember me"
          />
          <Button
            type="submit"
            fullWidth
            variant="contained"
            sx={{ mt: 3, mb: 2 }}
          >
            Sign Up
          </Button>
        
        </Box>

        <Button
            type="submit"
            fullWidth
            variant="contained"
            sx={{ mt: 1, mb: 1 }}
            style={{
              backgroundColor: "#FFFAFA",
            }}
            onClick={SignInGoogle}
          >
            Sign In with Google
          </Button>

        <Grid container>
            <Grid item>
              <Link href="/" variant="body2">
                {"Already have an account? Sign In"}
              </Link>
            </Grid>
          </Grid>
      </Box>
    </Container>
    </ThemeProvider>
  );
}
</file>

<file path="src/SummaryPage.js">
import { initializeApp } from 'firebase/app';
import { getFirestore, collection, onSnapshot, query, where, limit, orderBy } from 'firebase/firestore'
import * as React from 'react';
import { useState, useEffect } from "react";
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import Paper from '@mui/material/Paper';
import LinearProgress from '@mui/material/LinearProgress';
import List from '@mui/material/List';
import Button from '@mui/material/Button';
import ListItem from '@mui/material/ListItem';
import Divider from '@mui/material/Divider';
import ListItemText from '@mui/material/ListItemText';
import firebaseApp from './firebase-config';

// Connect to current firebase project
const firestore = getFirestore(firebaseApp);

/* Identify the current user */
const user_email = window.localStorage.getItem('user_email');

export default function SummaryPage() {
    const [users, setUsers] = useState([])
    const [connectors, setConnectors] = useState([])
    const [tasks, setTasks] = useState([])
    const [flag, setFlag] = useState(false)

    /* Current date */
    const currDate = new Date().toDateString()

    /* Firestore SDK queries */
    useEffect(() => {
        const userQuery = query(
        collection(firestore, 'users'),
        where('email', '==', user_email)
        );
        const unsubscribe = onSnapshot(userQuery, snapshot => {
            setUsers(snapshot.docs.map(doc => ({id: doc.id, data: doc.data() })))
        })

        return () => {
            unsubscribe()
        }
        }, [])

    useEffect(() => {
        const connectorQuery = query(
            collection(firestore, 'connectors'),
            where('user_email', '==', user_email),
            limit(6)
        );
        const unsubscribe = onSnapshot(connectorQuery, snapshot => {
            setConnectors(snapshot.docs.map(doc => ({id: doc.id, data: doc.data() })))
        })

        return () => {
            unsubscribe()
        }
        }, [])

    useEffect(() => {
        var alertQuery = query(
            collection(firestore, 'alerts'),
            where('email', '==', user_email),
            orderBy("time", "desc"),
            limit(5)
        );
        if (flag) {
            alertQuery = query(
                collection(firestore, 'alerts'),
                where('email', '==', user_email),
                orderBy("time", "desc")
            );
        }
        const unsubscribe = onSnapshot(alertQuery, snapshot => {
            setTasks(snapshot.docs.map(doc => ({id: doc.id, data: doc.data() })))
        })

        return () => {
            unsubscribe()
        }
        }, [flag])

    return (
        <Box>
            {/* Title */}
            <Box>
                <Typography
                    component="h1"
                    variant="h4"
                    color="inherit"
                    noWrap
                    sx={{ flexGrow: 1, mt: 5, ml: 10 }}
                >
                    Today is: {currDate}
                </Typography>

                {users?.map((row) => (
                    <Typography
                        component="h1"
                        variant="h5"
                        color="inherit"
                        noWrap
                        sx={{ flexGrow: 1, mt: 5, ml: 10 }}
                    >
                        Welcome, {row.data.firstName}
                    </Typography>
                ))}
            </Box>
            
            {/* Summary board */}
            <Box sx={{ ml: 5, mt: 5, border: 2, display: 'flex', minHeight: 400, width: '95%' }}>
                <Box sx={{ borderRight: 1, minWidth: 700 }}>
                    <Typography
                        component="h1"
                        variant="h6"
                        color="inherit"
                        noWrap
                        sx={{ flexGrow: 1, ml: 2, mt: 1, mb: 1 }}
                    >
                        Status of your feeds:
                    </Typography>

                    <List sx={{ bgcolor: 'rgba(71, 98, 130, 0.2)' }}>
                    {connectors?.map((row) => (
                        <ListItem divider='true'>
                            <ListItemText primary={row.data.id + '. ' + row.data.name} />
                            <Box sx={{ minWidth: 300, ml: 4, mr: 2 }}>
                                <LinearProgress variant="determinate" value={parseInt(row.data.status.substr(0, row.data.status.length - 1))} />
                            </Box>
                        </ListItem>
                    ))}
                    </List>
                </Box>

                <Box sx={{ width: '100%' }}>
                    <Box sx={{display: 'flex'}}>
                        <Typography
                            component="h1"
                            variant="h6"
                            color="inherit"
                            noWrap
                            sx={{ flexGrow: 1, ml: 2, mt: 1, mb: 1 }}
                        >
                            Alerts:
                        </Typography>
                        <Button onClick={()=>{setFlag(!flag)}}>
                            show all
                        </Button>
                    </Box>

                    <Paper style={{maxHeight: 400, overflow: 'auto'}}>
                        <List sx={{ bgcolor: 'rgba(71, 98, 130, 0.2)' }}>
                        {tasks?.map((row) => (
                            <ListItem divider='true'>
                                <ListItemText primary={row.data.content} secondary={row.data.date}/>
                            </ListItem>
                        ))}
                        </List>
                    </Paper>
                </Box>
            </Box>
        </Box>
    );
}
</file>

</files>
