


export const apiBaseUrl =
  window.globals.api.arcade && window.globals.api.arcade !== '${REACT_APP_ARCADE_API_URL}'
    ? `${window.globals.api.arcade}`
    : `${process.env.REACT_APP_ARCADE_API_URL}`;
