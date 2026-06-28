// Llamadas a la API del backend
import axios from 'axios'


export async function createForm(data) {
    const response = await axios.post('/form', data);
    return response
}

export async function getFormByEmail(email) {
    const data = await axios.get(`/form/user/${email}`)
    
    return data
}

export async function uploadFile(file) {
    const formData = new FormData();
    formData.append('image', file);
    const response = await axios.post('/form/attachment', formData);

    return response
}